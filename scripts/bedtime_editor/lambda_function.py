import json
import boto3
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup
import os
import hashlib

s3 = boto3.client('s3')
BUCKET_NAME = 'tl-web'
STORIES_PREFIX = 'stories/'
ALLOWED_ORIGINS = ['https://tl-web.s3.us-west-2.amazonaws.com']  # List of allowed origins
# Get allowed passwords from environment variable
ALLOWED_PASSWORDS = [pwd.strip() for pwd in os.environ.get('ALLOWED_PASSWORDS', '').split(',') if pwd.strip()]
print(f"Allowed passwords (masked): {['*' * len(pwd) for pwd in ALLOWED_PASSWORDS]}")

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        action = body.get('action')

        if action == 'update':
            return update_story(body)
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid action'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Internal Server Error: {str(e)}'})
        }

def get_story(event, headers):
    story_key = event['queryStringParameters']['key']
    
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=STORIES_PREFIX + story_key)
        story_content = response['Body'].read().decode('utf-8')
        
        # Parse HTML and extract story text
        soup = BeautifulSoup(story_content, 'html.parser')
        story_parts = soup.find_all('div', class_='story-part')
        
        extracted_text = []
        for part in story_parts:
            english = part.find('p').text
            tetun = part.find('p', class_='tetun').text
            extracted_text.append({'english': english, 'tetun': tetun})
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(extracted_text)
        }
    except ClientError as e:
        return {
            'statusCode': 404,
            'headers': headers,
            'body': json.dumps('Story not found')
        }

def update_story(body):
    key = body.get('key')
    content = body.get('content')
    password = body.get('password')

    if not key or not content or not password:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Missing key, content, or password'})
        }

    if password not in ALLOWED_PASSWORDS:
        return {
            'statusCode': 403,
            'body': json.dumps({'message': 'Invalid password'})
        }

    if not (key.lower().startswith('bedtime') and key.lower().endswith('.html')):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid file name. Only bedtime stories with .html extension are allowed.'})
        }

    try:
        s3.put_object(Bucket=BUCKET_NAME, Key=STORIES_PREFIX + key, Body=content, ContentType='text/html')
        
        # Calculate MD5 hash of the uploaded content
        md5_hash = hashlib.md5(content.encode()).hexdigest()
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Story updated successfully', 'md5': md5_hash})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Error updating S3: {str(e)}'})
        }