import boto3
import json
import requests
from datetime import datetime
import logging
import os
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TOPICS = [
    "Timor-Leste education",
    "Timor-Leste health",
    "Timor-Leste agriculture",
    "Timor-Leste tourism",
    "Timor-Leste jobs",
    "Timor-Leste government",
    "Timor-Leste environment",
    "Timor-Leste news",
    "Tetum language",
    "Timor-Leste finance",
    "Timor-Leste technology",
    "Timor-Leste sports"
]

# Load API key from environment variable
API_KEY = os.environ.get('API_KEY')

# Search Engine ID (cx)
SEARCH_ENGINE_ID = os.environ.get('SEARCH_ENGINE_ID')

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'tl-web'
    
    all_results = []
    
    for topic in TOPICS:
        results = search_topic(topic)
        all_results.extend(results)
        logger.info(f"Found {len(results)} results for topic: {topic}")
    
    today = datetime.now().strftime("%Y-%m-%d")
    file_name = f"tl_info_{today}.json"
    
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(all_results),
        ContentType='application/json'
    )
    
    logger.info(f"Uploaded {file_name} with {len(all_results)} total results")
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully uploaded {file_name} to S3')
    }

def search_topic(topic):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'cx': SEARCH_ENGINE_ID,
        'key': API_KEY,
        'q': topic,
        'num': 5  # Number of results to return
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for item in data.get('items', []):
            results.append({
                'topic': topic,
                'title': item.get('title', ''),
                'link': item.get('link', ''),
                'snippet': item.get('snippet', '')[:200] + '...',
                'source': 'Google Custom Search'
            })
        
        logger.info(f"Parsed {len(results)} results for {topic}")
        return results
    except Exception as e:
        logger.error(f"Failed to fetch results for {topic}: {str(e)}")
        return []

# For local testing
if __name__ == "__main__":
    print(json.dumps(lambda_handler({}, None), indent=2))