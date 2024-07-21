import json
import os
import re
import openai
import boto3
import urllib.parse
import json
import logging
import base64

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

S3_BUCKET = "tl-web"
DICTIONARY_KEY = "dictionary.js"
TEMPLATE_KEY = "template.html"

s3 = boto3.client('s3')
english_to_tetum = json.loads(s3.get_object(Bucket=S3_BUCKET, Key=DICTIONARY_KEY)['Body'].read().decode('utf-8').replace("english_to_tetum = ", "").rstrip(';'))
tetum_to_english = {v: k for k, v in english_to_tetum.items()}
HTML_TEMPLATE = s3.get_object(Bucket=S3_BUCKET, Key=TEMPLATE_KEY)['Body'].read().decode('utf-8')

openai.api_key = os.environ['OPENAI_API_KEY']

def clean_up_translation(text, direction):
    if not text:
        return "No text provided for refinement."

    if direction == 'engToTetum':
        prompt = f"As a linguist specializing in Tetum, please refine this Tetum translation if necessary, improving its grammar, punctuation, and capitalization while maintaining its original meaning. If the translation is already correct, please state that no changes are needed. Here's the text: {text}"
    else:  # tetumToEng
        prompt = f"As a linguist specializing in English, please refine this English translation if necessary, improving its grammar, punctuation, and capitalization while maintaining its original meaning. If the translation is already correct, please state that no changes are needed. Here's the text: {text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a skilled linguist with expertise in both English and Tetum languages. Your task is to refine the provided text while maintaining its original meaning. If the text is already correct, state that no changes are needed."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

def translate_words(text, dictionary):
    words = re.findall(r'\b\w+\b|[.,!?;]', text.lower())
    translated_words = [dictionary.get(word, word) for word in words]
    return ' '.join(translated_words)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    
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
        elif uri == '/translate' or uri == '/' or uri == '':
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

    elif method == 'POST' and (uri == '/translate' or uri == '/' or uri == ''):
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

        # Perform word-by-word translation
        if direction == 'engToTetum':
            initial_translation = translate_words(text, english_to_tetum)
        else:  # tetumToEng
            initial_translation = translate_words(text, tetum_to_english)

        logger.info(f"Initial translation: '{initial_translation}'")

        # Refine the translation
        refined_translation = clean_up_translation(initial_translation, direction)
        logger.info(f"Refined translation: '{refined_translation}'")

        # Check if the refinement suggests no changes
        if "no changes are needed" in refined_translation.lower():
            final_translation = initial_translation
        else:
            final_translation = refined_translation

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