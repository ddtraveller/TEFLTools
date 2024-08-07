import json
import requests
import os
import re
import anthropic
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.environ.get('SEARCH_ENGINE_ID')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')

anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def format_entry(entry):
    return f"{entry['title']}\n{entry['link']}\n"

def lambda_handler(event, context):
    logger.debug(f"Received event: {json.dumps(event)}")

    cors_headers = {
        'Access-Control-Allow-Origin': 'https://go-tl.com',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }

    # Handle OPTIONS request
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': json.dumps('OK')
        }

    try:
        if event.get('body'):
            try:
                body = json.loads(event['body'])
            except json.JSONDecodeError:
                body = event['body']
        else:
            body = event

        full_question = body.get('question', '')
        logger.info(f"Processed question: {full_question}")

        # Extract the actual question from the translated text
        match = re.search(r"'(.+)'", full_question)
        if match:
            question = match.group(1)
        else:
            question = full_question

        if not question:
            logger.warning("No question provided")
            return {
                'statusCode': 400,
                'headers': cors_headers,
                'body': json.dumps({'error': 'No question provided'})
            }

        search_results = search_google(question)

        formatted_string = "\n".join(format_entry(entry) for entry in search_results)
        logger.info(f"Format Entry: {json.dumps(formatted_string)}")
        final_answer = generate_answer_and_summaries(question, formatted_string)
        logger.info(f"Generated answer: {final_answer}")

        response = {
            'question': full_question,
            'answer': final_answer
        }

        logger.info(f"Final response: {json.dumps(response)}")

        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': json.dumps(response)
        }

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': cors_headers,
            'body': json.dumps({'error': 'An unexpected error occurred'})
        }

def search_google(query):
    logger.info(f"Searching Google for: {query}")
    logger.debug(f"GOOGLE_API_KEY: {'*' * len(GOOGLE_API_KEY)}")
    logger.debug(f"SEARCH_ENGINE_ID: {SEARCH_ENGINE_ID}")

    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'cx': SEARCH_ENGINE_ID,
        'key': GOOGLE_API_KEY,
        'q': query,
        'num': 5
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        logger.debug(f"Google API response: {json.dumps(data)}")

        results = [
            {
                'title': item.get('title', ''),
                'link': item.get('link', ''),
                'snippet': item.get('snippet', '')
            }
            for item in data.get('items', [])
        ]
        logger.info(f"Search results: {json.dumps(results)}")
        return results
    except requests.exceptions.RequestException as e:
        logger.error(f"Error in Google search: {str(e)}")
        return []

def extract_text_from_html(html_content):
    html_content = re.sub(r'<script\b[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<style\b[^>]*>.*?</style>', '', html_content, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', '', html_content)
    return re.sub(r'\s+', ' ', text).strip()

def generate_answer_and_summaries(question, content_summaries):
    logger.info("Generating answer and summaries")

    # Extract just the URLs from content_summaries
    urls = re.findall(r'https?://\S+', content_summaries)
    url_prompt = "\n".join(f"Link {i+1}: {url}" for i, url in enumerate(urls[:5]))

    prompt = f"""Question: {question}
Please provide:
1. A comprehensive answer to the question in a complete sentence or paragraph.
2. Use the following URLs as resources for your answer. List each link and briefly describe how it relates to the question:

{url_prompt}

Answer:
"""

    try:
        response = anthropic_client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            temperature=0.7,
            system="You are an advice columnist that provides opinions, answers and summaries based on given information.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        response_text = response.content[0].text.strip()

        return response_text
    except Exception as e:
        logger.error(f"Error in generate_answer_and_summaries: {str(e)}")
        return "An error occurred while generating the answer."