import json
import boto3
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup
import os
import hashlib
import re
from gtts import gTTS
from io import BytesIO
import requests
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3 = boto3.client('s3')
BUCKET_NAME = 'tl-web'
STORIES_PREFIX = 'stories/'
ALLOWED_ORIGINS = ['https://tl-web.s3.us-west-2.amazonaws.com', 'https://go-tl.com']
ALLOWED_PASSWORDS = [pwd.strip() for pwd in os.environ.get('ALLOWED_PASSWORDS', '').split(',') if pwd.strip()]
STABILITY_API_KEY = os.environ['STABILITY_API_KEY']

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        action = body.get('action')
        if action == 'update':
            return update_story(body)
        elif action == 'update_sounds':
            return update_sounds(body)
        elif action == 'replace_image':
            return replace_image(body)
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

def replace_image(body):
    key = body.get('key')
    story_name = body.get('story_name')
    part_number = body.get('part_number')
    part_description = body.get('part_description')
    style_preset = body.get('style_preset')
    is_first_image = body.get('is_first_image', 'n') == 'y'
    password = body.get('password')

    logger.info(f"Attempting to replace image for story: {story_name}, part: {part_number}")
    logger.info(f"HTML file key: {key}")

    if not all([key, story_name, part_number, part_description, style_preset, password]):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Missing required parameters'})
        }
    if password not in ALLOWED_PASSWORDS:
        return {
            'statusCode': 403,
            'body': json.dumps({'message': 'Invalid password'})
        }

    try:
        # Check if the key exists in the bucket
        try:
            s3.head_object(Bucket=BUCKET_NAME, Key=key)
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                logger.error(f"The HTML file does not exist: {key}")
                # If the key doesn't exist, try prepending 'stories/'
                alternative_key = f"stories/{key}"
                logger.info(f"Trying alternative key: {alternative_key}")
                try:
                    s3.head_object(Bucket=BUCKET_NAME, Key=alternative_key)
                    key = alternative_key
                except ClientError:
                    return {
                        'statusCode': 404,
                        'body': json.dumps({'message': f'HTML file not found: {key} or {alternative_key}'})
                    }
            else:
                raise

        # Get the current HTML content
        response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
        html_content = response['Body'].read().decode('utf-8')

        # Parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the image to replace
        img_tag = soup.select_one(f'.story-part:nth-of-type({int(part_number) + 1}) img')
        if not img_tag:
            logger.error(f"Image not found for part {part_number}")
            return {
                'statusCode': 400,
                'body': json.dumps({'message': f'Image not found for part {part_number}'})
            }

        # Extract the current image name from the src attribute
        current_image_src = img_tag['src']
        current_image_name = os.path.basename(current_image_src)
        logger.info(f"Current image src: {current_image_src}")
        logger.info(f"Current image name: {current_image_name}")

        # Generate the new image
        new_image = generate_new_image(part_description, style_preset, is_first_image, int(part_number))
        if not new_image:
            logger.error("Failed to generate new image")
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Failed to generate new image'})
            }

        # Construct the new image key
        new_image_key = f'images/{current_image_name}'

        # Upload the new image to S3
        s3.put_object(Bucket=BUCKET_NAME, Key=new_image_key, Body=new_image.getvalue(), ContentType='image/png')
        logger.info(f"New image uploaded to: {new_image_key}")

        # Update the image tag in the HTML
        img_tag['src'] = f'/{new_image_key}'

        # Upload the updated HTML back to S3
        updated_html = str(soup)
        s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=updated_html, ContentType='text/html')
        logger.info(f"Updated HTML uploaded to: {key}")

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Image replaced successfully'})
        }
    except Exception as e:
        logger.error(f"Error replacing image: {str(e)}", exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Error replacing image: {str(e)}'})
        }
        
def generate_new_image(prompt, style_preset, is_first_image, part_number=1):
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "Accept": "image/*",
        "Authorization": f"Bearer {STABILITY_API_KEY}"
    }

    story_instruction = f"Create a whimsical, child-friendly {style_preset} illustration for a bedtime story. Generate the image for part {part_number}."
    consistency_prompt = "Create a consistent style for the story." if is_first_image else "Maintain style consistency with previous illustrations."
    style_prompt = """
    Use a vibrant, colorful palette reminiscent of Jaime Hernandez's work in Love and Rockets.
    Character designs should blend realistic proportions with slightly exaggerated features, similar to an anime style.
    Architecture should be gigantic, whimsical, ultra technical or magical or cosmic. Very comic book. 
    Flora and fauna should me mythical, magical, diverse and local to Timor Leste.
    Include details that reflect Timorese culture, such as traditional tais textiles, uma lulik (sacred houses), local flora and fauna, and Inan Nunu; the Divine Mother who nourishes all in this land.
    Mix ultra post-modern and ancient anachronistic elements to create a unique, futuristic Timorese aesthetic.
    Use dynamic compositions and dramatic angles inspired by comic book panels.
    Incorporate subtle magical or fantastical elements that blend seamlessly with the realistic setting.
    Emphasize expressive character faces and body language to convey emotions.
    Use lighting effects to create mood and atmosphere, especially for scenes set at different times of day.    
    Use a vibrant, bold color palette with rich, saturated hues, particularly emphasizing warm oranges, deep teals, and lush greens.
    Employ a comic book or graphic novel art style with clean, defined outlines and flat colors.
    Create detailed, fantastical backgrounds that blend natural elements (like the mushroom-like trees) with cosmic imagery (planets and stars).
    Use perspective to create a sense of wonder, such as positioning the viewer to look up at towering flora or celestial objects.
    Incorporate small, whimsical details like floating particles or small creatures to add life to the scene.
    Ensure character clothing is simple yet modern, with solid colors that stand out against the busy background.
    Use subtle gradients and shading to add dimension to flat color areas, especially on larger objects like planets.
    """
    full_prompt = f"{story_instruction} {prompt} {style_prompt} {consistency_prompt}"

    payload = {
        "prompt": (None, full_prompt),
        "negative_prompt": (None, ""),
        "output_format": (None, "png"),
        "cfg_scale": (None, "15"),
        "clip_guidance_preset": (None, "SLOWEST"),
        "height": (None, "576"),
        "width": (None, "1024"),
        "samples": (None, "1"),
        "steps": (None, "50"),
        "style_preset": (None, style_preset),
        "model": (None, "sd3-large"),
        "seed": (None, "3994967295")
    }

    max_retries = 5
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}: Sending request")
            response = requests.post(url, headers=headers, files=payload)
            response.raise_for_status()

            if response.headers['Content-Type'].startswith('image/'):
                return BytesIO(response.content)
            else:
                raise Exception(f"Unexpected content type: {response.headers['Content-Type']}")
        except requests.exceptions.RequestException as e:
            print(f"Error generating image on attempt {attempt + 1}: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response content: {e.response.content}")

            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise

    print('Image generation failure after all attempts')
    return None