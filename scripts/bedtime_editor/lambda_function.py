import json
import boto3
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup
import os

s3 = boto3.client('s3')
BUCKET_NAME = 'tl-web'
STORIES_PREFIX = 'stories/'
ALLOWED_ORIGINS = ['https://tl-web.s3.us-west-2.amazonaws.com']  # List of allowed origins
# Get allowed passwords from environment variable
ALLOWED_PASSWORDS = [pwd.strip() for pwd in os.environ.get('ALLOWED_PASSWORDS', '').split(',') if pwd.strip()]
print(f"Allowed passwords (masked): {['*' * len(pwd) for pwd in ALLOWED_PASSWORDS]}")

def lambda_handler(event, context):
    # Get the origin from the request
    origin = event.get('headers', {}).get('origin') or event.get('headers', {}).get('Origin')
    
    # Set CORS headers
    headers = {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    }
    
    # Set the Access-Control-Allow-Origin header only if the origin is allowed
    if origin in ALLOWED_ORIGINS:
        headers['Access-Control-Allow-Origin'] = origin
    
    # Handle preflight request
    if event.get('requestContext', {}).get('http', {}).get('method') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps('OK')
        }
    
    try:
        # Parse the incoming request body
        body = json.loads(event.get('body', '{}'))
        action = body.get('action')
        
        if action == 'update':
            key = body.get('key')
            content = body.get('content')
            
            if not key or not content:
                raise ValueError("Missing key or content in the request")
            
            # Update the S3 object
            update_story(body, headers)
            
            print(f"Story updated successfully: {STORIES_PREFIX + key}")
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps('Story updated successfully')
            }
        else:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps('Invalid action')
            }
    except json.JSONDecodeError:
        print("Error: Invalid JSON in request body")
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps('Invalid JSON in request body')
        }
    except ValueError as ve:
        print(f"Error: {str(ve)}")
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps(f'Bad Request: {str(ve)}')
        }
    except ClientError as e:
        print(f"Error updating S3: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps(f'Error updating S3: {str(e)}')
        }
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps(f'Internal Server Error: {str(e)}')
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

def update_story(body, headers):
    key = body.get('key')
    content = body.get('content')
    password = body.get('password')
    
    print(f"Attempting to update story: {key}")
    
    if not key or not content or not password:
        print("Missing key, content, or password in the request")
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({'message': 'Missing key, content, or password in the request'})
        }
    
    # Check password with exact match
    password_valid = False
    for allowed_password in ALLOWED_PASSWORDS:
        if password == allowed_password:
            password_valid = True
            break
    
    print(f"Password check result: {'Valid' if password_valid else 'Invalid'}")
    
    if not password_valid:
        print("Invalid password provided")
        return {
            'statusCode': 403,
            'headers': headers,
            'body': json.dumps({'message': 'Invalid password'})
        }
    
    # Check if the file name starts with 'bedtime' and ends with '.html'
    if not (key.lower().startswith('bedtime') and key.lower().endswith('.html')):
        print(f"Invalid file name: {key}")
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({'message': 'Invalid file name. Only bedtime stories with .html extension are allowed.'})
        }
    
    try:
        # Update the S3 object
        s3.put_object(Bucket=BUCKET_NAME, Key=STORIES_PREFIX + key, Body=content, ContentType='text/html')
        
        print(f"Story updated successfully: {STORIES_PREFIX + key}")
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': 'Story updated successfully'})
        }
    except ClientError as e:
        print(f"Error updating S3: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'message': f'Error updating S3: {str(e)}'})
        }