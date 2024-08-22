import json
import boto3
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup
import os
import hashlib
import re
from gtts import gTTS
from io import BytesIO

s3 = boto3.client('s3')
BUCKET_NAME = 'tl-web'
STORIES_PREFIX = 'stories/'
ALLOWED_ORIGINS = ['https://tl-web.s3.us-west-2.amazonaws.com']
ALLOWED_PASSWORDS = [pwd.strip() for pwd in os.environ.get('ALLOWED_PASSWORDS', '').split(',') if pwd.strip()]

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        action = body.get('action')
        if action == 'update':
            return update_story(body)
        elif action == 'update_sounds':
            return update_sounds(body)
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

def update_sounds(body):
    key = body.get('key')
    password = body.get('password')
    if not key or not password:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Missing key or password'})
        }
    if password not in ALLOWED_PASSWORDS:
        return {
            'statusCode': 403,
            'body': json.dumps({'message': 'Invalid password'})
        }
    try:
        # Get the HTML content
        response = s3.get_object(Bucket=BUCKET_NAME, Key=STORIES_PREFIX + key)
        html_content = response['Body'].read().decode('utf-8')

        # Parse HTML and extract audio data
        soup = BeautifulSoup(html_content, 'html.parser')
        audio_data = []
        for div in soup.find_all('div', class_='story-part'):
            part_number = div.find('h2')
            if part_number is None:
                continue  # Skip this div if it doesn't have an h2 tag
            part_number = part_number.text.strip()
            
            text_p = div.find('p')
            if text_p is None:
                continue  # Skip this div if it doesn't have a p tag
            text = text_p.text.strip()
            
            audio_tag = div.find('audio')
            if audio_tag and audio_tag.find('source'):
                audio_url = audio_tag.find('source')['src']
                audio_filename = audio_url.split('/')[-1]
                audio_data.append({
                    'part': part_number,
                    'text': text,
                    'filename': audio_filename
                })

        if not audio_data:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'No audio data found in the HTML'})
            }

        # Generate and replace sound files
        for item in audio_data:
            generate_sound(item['text'], item['filename'])

        # Update the HTML content
        for item in audio_data:
            div = soup.find('div', class_='story-part', string=lambda text: item['part'] in text if text else False)
            if div:
                audio_tag = div.find('audio')
                if audio_tag:
                    source_tag = audio_tag.find('source')
                    if source_tag:
                        source_tag['src'] = f'sounds/{item["filename"]}'

        # Upload the updated HTML back to S3
        updated_html = str(soup)
        s3.put_object(Bucket=BUCKET_NAME, Key=STORIES_PREFIX + key, Body=updated_html, ContentType='text/html')

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Sounds updated successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Error updating sounds: {str(e)}'})
        }

def generate_sound(text, filename):
    # Replace apostrophes with empty strings
    text = text.replace("'", "")
    text = re.sub(r'Part \d+$', '', text).strip()
    
    # Create a gTTS object with the given text and language
    tts = gTTS(text=text, lang='en', tld='co.uk')
    
    # Create a BytesIO object to store the audio data
    fp = BytesIO()
    
    # Write the audio data to the BytesIO object
    tts.write_to_fp(fp)
    
    # Move the file pointer to the beginning of the BytesIO object
    fp.seek(0)
    
    # Save the audio data to S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f'sounds/{filename}',
        Body=fp,
        ContentType='audio/mpeg'
    )