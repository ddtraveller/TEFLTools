import json
import os
import re
import urllib.parse
import logging
import base64
from anthropic import Anthropic
import tiktoken

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

anthropic_client = Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

# Load JSON files from the Lambda package
try:
    with open('dictionary.json', 'r') as file:
        english_to_tetum = json.load(file)
    with open('phrases.json', 'r') as file:
        phrases = json.load(file)
    with open('compound.json', 'r') as file:
        compound = json.load(file)
except FileNotFoundError as e:
    logger.error(f"Error loading JSON files: {str(e)}")
    raise
except json.JSONDecodeError as e:
    logger.error(f"Error parsing JSON files: {str(e)}")
    raise

# Load prompt files
try:
    with open('E2T.txt', 'r') as file:
        E2T_PROMPT = file.read()
    with open('T2E.txt', 'r') as file:
        T2E_PROMPT = file.read()
except FileNotFoundError as e:
    logger.error(f"Error loading prompt files: {str(e)}")
    raise

try:
    logger.debug("Loading HTML template from Lambda package")
    with open('template.html', 'r') as file:
        HTML_TEMPLATE = file.read()
except FileNotFoundError as e:
    logger.error(f"Error loading HTML template: {str(e)}")
    raise

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    logger.debug(f"Counting tokens for string of length {len(string)}")
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    logger.debug(f"Token count: {num_tokens}")
    return num_tokens

def translate(original_text, direction):
    logger.debug(f"Starting translation. Direction: {direction}")

    if not original_text:
        logger.warning("No text provided for translation")
        return "No text provided for translation."

    try:
        input_tokens = num_tokens_from_string(original_text)
        max_tokens = min(4000, input_tokens * 2)
        logger.debug(f"Set max_tokens to {max_tokens}")
        
        if direction == 'engToTetum':
            prompt = E2T_PROMPT.format(
                english_to_tetum=json.dumps(english_to_tetum),
                phrases=json.dumps(phrases),
                compound=json.dumps(compound),
                original_text=original_text
            )
        else:  # tetumToEng
            prompt = T2E_PROMPT.format(original_text=original_text)
        
        logger.debug("Sending request to Anthropic API")
        response = anthropic_client.completions.create(
            prompt=prompt,
            model="claude-v1",
            max_tokens_to_sample=max_tokens,
            stop_sequences=["\n\nHuman:"]
        )
        
        final_translation = response.completion.strip()
        
        logger.debug("Received final translation from Anthropic API")
        return final_translation
    except Exception as e:
        logger.error(f"Error in translation: {str(e)}")
        raise

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    
    try:
        # Check if the event is from CloudFront
        if 'Records' in event and 'cf' in event['Records'][0]:
            cf_request = event['Records'][0]['cf']['request']
            method = cf_request['method']
            uri = cf_request['uri']
            is_cloudfront = True
        else:
            # Fallback to direct Lambda invocation format
            method = event['requestContext']['http']['method']
            uri = event.get('rawPath', '')
            is_cloudfront = False

        logger.info(f"HTTP method: {method}")
        logger.info(f"URI: {uri}")

        if method == 'GET':
            if uri == '/favicon.ico':
                return {'statusCode': 204, 'body': ''} if not is_cloudfront else {'status': '204', 'body': ''}
            elif uri == '/translate' or uri == '/' or uri == '' or uri == '/2way':
                html = HTML_TEMPLATE.replace('PLACEHOLDER_TEXT', '').replace('PLACEHOLDER_TRANSLATION', '')
                html = html.replace('PLACEHOLDER_ENG_CHECKED', 'checked').replace('PLACEHOLDER_TETUM_CHECKED', '')
                if is_cloudfront:
                    return {
                        'status': '200',
                        'headers': {'content-type': [{'key': 'Content-Type', 'value': 'text/html'}]},
                        'body': html
                    }
                else:
                    return {'statusCode': 200, 'headers': {'Content-Type': 'text/html'}, 'body': html}

        elif method == 'POST' and (uri == '/translate' or uri == '/' or uri == '' or uri == '/2way'):
            logger.info("Received POST request")
            
            # Get body
            if is_cloudfront:
                body = cf_request.get('body', {})
                if body.get('encoding') == 'base64':
                    body = base64.b64decode(body['data']).decode('utf-8')
                else:
                    body = body.get('data', '')
            else:
                body = event.get('body', '')
                is_base64_encoded = event.get('isBase64Encoded', False)
                if is_base64_encoded:
                    body = base64.b64decode(body).decode('utf-8')
            
            logger.info(f"Raw body: {body}")

            # Parse body
            parsed_body = urllib.parse.parse_qs(body)
            logger.info(f"Parsed body: {json.dumps(parsed_body)}")

            # Extract text and direction
            text = parsed_body.get('text', [''])[0]
            direction = parsed_body.get('direction', ['engToTetum'])[0]

            logger.info(f"Extracted text: '{text}'")
            logger.info(f"Extracted direction: '{direction}'")

            if not text:
                error_response = 'No text provided for translation'
                if is_cloudfront:
                    return {
                        'status': '400',
                        'headers': {'content-type': [{'key': 'Content-Type', 'value': 'text/plain'}]},
                        'body': error_response
                    }
                else:
                    return {'statusCode': 400, 'body': json.dumps(error_response)}

            # Check word count
            word_count = len(text.split())
            if word_count > 400:
                error_response = 'Text exceeds 400 word limit. Please shorten your text and try again.'
                if is_cloudfront:
                    return {
                        'status': '400',
                        'headers': {'content-type': [{'key': 'Content-Type', 'value': 'text/plain'}]},
                        'body': error_response
                    }
                else:
                    return {'statusCode': 400, 'body': json.dumps(error_response)}

            # Perform translation
            final_translation = translate(text, direction)
            logger.info(f"Final translation: '{final_translation}'")

            html = HTML_TEMPLATE.replace('PLACEHOLDER_TEXT', text).replace('PLACEHOLDER_TRANSLATION', final_translation)
            html = html.replace('PLACEHOLDER_ENG_CHECKED', 'checked' if direction == 'engToTetum' else '')
            html = html.replace('PLACEHOLDER_TETUM_CHECKED', 'checked' if direction == 'tetumToEng' else '')

            if is_cloudfront:
                return {
                    'status': '200',
                    'headers': {'content-type': [{'key': 'Content-Type', 'value': 'text/html'}]},
                    'body': html
                }
            else:
                return {'statusCode': 200, 'headers': {'Content-Type': 'text/html'}, 'body': html}

        # Handle not found
        not_found_response = 'Not Found'
        if is_cloudfront:
            return {
                'status': '404',
                'headers': {'content-type': [{'key': 'Content-Type', 'value': 'text/plain'}]},
                'body': not_found_response
            }
        else:
            return {'statusCode': 404, 'body': json.dumps(not_found_response)}
    except Exception as e:
        logger.error(f"Error in Lambda handler: {str(e)}")
        error_response = 'Internal Server Error'
        if is_cloudfront:
            return {
                'status': '500',
                'headers': {'content-type': [{'key': 'Content-Type', 'value': 'text/plain'}]},
                'body': error_response
            }
        else:
            return {'statusCode': 500, 'body': json.dumps(error_response)}