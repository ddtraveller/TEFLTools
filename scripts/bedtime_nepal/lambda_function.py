import json
import random
import os
import boto3
from anthropic import Anthropic
import requests
from io import BytesIO
from datetime import datetime
import base64  
import re
import tiktoken
from pathlib import Path
from random import choice, shuffle
import colorsys
import time
import traceback
from lark import Lark, Transformer
from gtts import gTTS
import sys
import anthropic
import urllib.parse
from requests_toolbelt import MultipartEncoder

# Set up paths (assuming the script is in the same directory as the JSON files)
SCRIPT_DIR = Path(__file__).resolve().parent
DICT_FILE = SCRIPT_DIR / 'dictionary.json'
PHRASES_FILE = SCRIPT_DIR / 'phrases.json'
COMPOUND_FILE = SCRIPT_DIR / 'compound.json'
RANDOM_ELEMENTS_FILE = SCRIPT_DIR / 'random_elements.json'
ALLOWED_ORIGINS = ['https://tl-web.s3.us-west-2.amazonaws.com', 'https://go-tl.com']

ALLOWED_PASSWORDS = [
    pwd.strip() 
    for pwd in urllib.parse.unquote(os.environ.get('ALLOWED_PASSWORDS', '')).split(',') 
    if pwd.strip()
]

# Load random elements from file
def load_random_elements():
    with open(RANDOM_ELEMENTS_FILE, 'r') as file:
        elements = json.load(file)
    shuffle(elements)  # Shuffle the elements
    return elements

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
        Bucket='tl-web',
        Key=f'sounds/{filename}',
        Body=fp,
        ContentType='audio/mpeg'
    )
    
    return f'https://tl-web.s3.us-west-2.amazonaws.com/sounds/{filename}'
    
# Load dictionary, phrases, and compounds
def load_dict_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
# Initialize clients
anthropic_client = Anthropic(
    api_key=os.environ['ANTHROPIC_API_KEY'],
    max_retries=3  # Add retry configuration
)
s3 = boto3.client('s3')
stability_api_key = os.environ['STABILITY_API_KEY']

def load_random_file():
    s3_object = s3.get_object(Bucket='tl-web', Key='files.json')
    files_data = json.loads(s3_object['Body'].read().decode('utf-8'))
    random_file = random.choice(files_data['files'])
    return random_file['path']
        
def save_image_to_s3(image_data, image_name):
    # Truncate the image name if it's too long
    if len(image_name) > 100:
        # Keep the date and image number, but truncate the title
        parts = image_name.split('_')
        date_part = parts[-2]
        number_part = parts[-1]
        title_part = '_'.join(parts[:-2])[:50]  # Truncate to 50 chars
        image_name = f"{title_part}__{date_part}_{number_part}"
    
    print(f"Saving image with name: {image_name}")
    
    s3.put_object(
        Bucket='tl-web',
        Key=f'images/{image_name}',
        Body=image_data.getvalue(),
        ContentType='image/png'
    )
    return f'images/{image_name}'

# Function to count tokens in a string
def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def generate_pastel_color():
    h = random.random()
    s = 0.25 + random.random() * 0.25  # 0.25 to 0.5
    l = 0.85 + random.random() * 0.1  # 0.85 to 0.95
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return f"rgb({int(r*255)}, {int(g*255)}, {int(b*255)})"

def generate_html(story, image_urls, sound_urls):
    background_color = generate_pastel_color()
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{story['title']['english']}</title>
        <link rel="icon" href="https://tl-web.s3.us-west-2.amazonaws.com/images/flag.jpg" type="image/png">
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: {background_color};
            }}
            h1 {{
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
                font-size: 2.5em;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
                margin-top: 40px;
            }}
            .story-part {{
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 30px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            img {{
                max-width: 100%;
                height: auto;
                margin-bottom: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }}
            .tetun {{
                font-style: italic;
                color: #555;
                background-color: rgba(255, 255, 255, 0.5);
                padding: 10px;
                border-radius: 5px;
                margin-top: 10px;
            }}
            audio {{
                width: 100%;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>{story['title']['tetun']}</h1>
        <h1>{story['title']['english']}</h1>
    """
    
    for i, part in enumerate(story['parts'], 1):
        english_text = re.sub(r'\s*Part \d+\s*$', '', part['english'].strip())
        tetun_text = part['tetun'].strip()
        image_url = image_urls[i-1] if i <= len(image_urls) else ""
        sound_url = sound_urls[i-1] if i <= len(sound_urls) else ""
        
        html += f"""
        <div class="story-part">
            <h2>Part {i}</h2>
            <p>{english_text}</p>
            <p class="tetun">{tetun_text}</p>
        """
        
        if image_url:
            html += f'<img src="{image_url}" alt="Story illustration {i}">'
        
        if sound_url:
            html += f"""
            <audio controls>
                <source src="{sound_url}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
            """
        
        html += "</div>"
    
    html += """
    <p><a href="https://go-tl.com/stories/archive.html">Arkivu Istória nian / Story Archive</a></p>
    <p><a href="https://go-tl.com/stories/editor.html">Editór Istória nian / Story Editor</a></p>
    </body>
    </html>
    """
    
    return html
    
def generate_image_gallery():
    bucket_name = 'tl-web'
    prefix = 'images/'
    
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    objects = response.get('Contents', [])
    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Gallery</title>
        <link rel="icon" href="https://tl-web.s3.us-west-2.amazonaws.com/images/flag.jpg" type="image/png">
        <style>
            .gallery {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                grid-gap: 20px;
            }
            .gallery img {
                width: 100%;
                height: auto;
            }
        </style>
    </head>
    <body>
        <h1>Image Gallery</h1>
        <div class="gallery">
    """
    
    for obj in objects:
        image_key = obj['Key']
        image_url = f"https://{bucket_name}.s3.amazonaws.com/{image_key}"
        html += f'<a href="{image_url}" target="_blank"><img src="{image_url}" alt="{image_key}"></a>'
    
    html += """
        </div>
    </body>
    </html>
    """
    
    s3.put_object(
        Bucket=bucket_name,
        Key='images/images.html',
        Body=html,
        ContentType='text/html'
    )

def parse_parts(content):
    parts = []
    current_part = {'part_number': 0, 'english': '', 'tetun': ''}
    
    for item in content:
        part_match = re.search(r'Part (\d+)', item)
        if part_match:
            if current_part['part_number'] != 0:
                parts.append(current_part)
                current_part = {'part_number': 0, 'english': '', 'tetun': ''}
            current_part['part_number'] = int(part_match.group(1))
        
        english_match = re.search(r'\(English\):(.*?)(?=\(Tetun\)|$)', item, re.DOTALL)
        tetun_match = re.search(r'\(Tetun\):(.*)', item, re.DOTALL)
        
        if english_match:
            current_part['english'] += english_match.group(1).strip() + ' '
        if tetun_match:
            current_part['tetun'] += tetun_match.group(1).strip() + ' '
        
        # Handle cases where English and Tetun are in separate items
        if not english_match and not tetun_match:
            if '(English)' in item:
                current_part['english'] += re.sub(r'^.*?\(English\):', '', item).strip() + ' '
            elif '(Tetun)' in item:
                current_part['tetun'] += re.sub(r'^.*?\(Tetun\):', '', item).strip() + ' '
    
    if current_part['part_number'] != 0:
        parts.append(current_part)
    
    # Sort parts by part number and clean up content
    parts.sort(key=lambda x: x['part_number'])
    for part in parts:
        part['english'] = re.sub(r'\s*Part \d+\s*$', '', part['english'].strip())
        part['tetun'] = re.sub(r'\s*Part \d+\s*$', '', part['tetun'].strip())
    
    return parts

def fallback_parse_parts(content):
    parts = []
    current_part = {'part_number': 0, 'english': '', 'tetun': ''}
    
    for item in content:
        part_match = re.search(r'Part (\d+)', item)
        if part_match:
            if current_part['part_number'] != 0:
                parts.append(current_part)
                current_part = {'part_number': 0, 'english': '', 'tetun': ''}
            current_part['part_number'] = int(part_match.group(1))
        
        english_match = re.search(r'\(English\):(.*?)(?=\(Tetun\)|$)', item, re.DOTALL)
        if english_match:
            current_part['english'] += english_match.group(1).strip() + ' '
        
        tetun_match = re.search(r'\(Tetun\):(.*)', item, re.DOTALL)
        if tetun_match:
            current_part['tetun'] += tetun_match.group(1).strip() + ' '
    
    if current_part['part_number'] != 0:
        parts.append(current_part)
    
    # Sort parts by part number
    parts.sort(key=lambda x: x['part_number'])
    
    return [
        {
            'part_number': part['part_number'],
            'english': part['english'].strip(),
            'tetun': part['tetun'].strip()
        }
        for part in parts
    ]

def parse_parts_marker_based(content):
    parts = []
    full_content = ' '.join(content)
    part_markers = ['Part 1', 'Part 2', 'Part 3', 'Part 4', 'Part 5', 'Part 6', 'Part 7']
    for i, marker in enumerate(part_markers):
        start = full_content.find(marker)
        if start == -1:
            continue
        end = full_content.find(part_markers[i+1]) if i+1 < len(part_markers) else len(full_content)
        part_content = full_content[start:end]
        part = {'part_number': int(marker.split()[1]), 'english': '', 'tetun': ''}
        
        english_match = re.search(r'\(English\):(.*?)(?=\(Tetun\)|$)', part_content, re.DOTALL)
        if english_match:
            part['english'] = english_match.group(1).strip()
        
        tetun_match = re.search(r'\(Tetun\):(.*)', part_content, re.DOTALL)
        if tetun_match:
            part['tetun'] = tetun_match.group(1).strip()
        
        parts.append(part)
    
    return parts

def parse_parts_lark(content):
    grammar = """
    start: part+
    part: "Part" NUMBER "(" LANG "):" text "(" LANG "):" text
    text: /[^(]*/
    NUMBER: /\d+/
    LANG: "English" | "Tetun"
    %import common.WS
    %ignore WS
    """
    
    class TreeToDict(Transformer):
        def part(self, items):
            return {
                'part_number': int(items[1]),
                'english': items[3].strip() if items[2] == 'English' else items[7].strip(),
                'tetun': items[7].strip() if items[2] == 'English' else items[3].strip()
            }
        
        def start(self, items):
            return items
    
    parser = Lark(grammar, parser='lalr', transformer=TreeToDict())
    
    try:
        full_content = ' '.join(content)
        return parser.parse(full_content)
    except Exception as e:
        print(f"Lark parsing failed: {str(e)}")
        return []

def fallback_title_parser(raw_content):
    lines = raw_content.strip().split('\n')
    english_title = ""
    tetun_title = ""
    
    for line in lines:
        if "English" in line and ":" in line:
            english_title = line.split(":", 1)[1].strip()
        elif "Tetun" in line and ":" in line:
            tetun_title = line.split(":", 1)[1].strip()
        elif line.startswith("Title (English):"):
            english_title = line.split(":", 1)[1].strip()
        elif line.startswith("Title (Tetun):"):
            tetun_title = line.split(":", 1)[1].strip()
        
        if english_title and tetun_title:
            break
    
    # If we still don't have both titles, try to find any line that looks like a title
    if not english_title or not tetun_title:
        for line in lines:
            if not english_title and not line.startswith("Part") and ":" not in line:
                english_title = line.strip()
            elif not tetun_title and not line.startswith("Part") and ":" not in line:
                tetun_title = line.strip()
            if english_title and tetun_title:
                break
    
    return {'english': english_title, 'tetun': tetun_title}
    
def truncate_text(text, max_tokens=3000):
    """Truncate text to stay within token limits"""
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
        return encoding.decode(tokens)
    return text

def generate_story(seed_file, story_prompt_template, story_seed):
    max_retries = 3
    retry_delay = 5  # seconds

    for attempt in range(max_retries):
        try:
            # Truncate inputs to stay within limits
            truncated_seed = truncate_text(story_seed, 500)  # Smaller limit for seed
            truncated_file = truncate_text(seed_file, 1500)  # Larger limit for file content
            
            # Format the prompt template with truncated inputs
            formatted_prompt = story_prompt_template.format(
                seed_file=truncated_file,
                story_seed=truncated_seed,
                selected_culture="Nepal"
            )
            
            # Check total prompt length
            total_tokens = num_tokens_from_string(formatted_prompt)
            print(f"Total input tokens: {total_tokens}")
            
            # Calculate safe max_tokens value
            # Leave room for the response while staying under Claude's limit
            max_output_tokens = min(4096 - total_tokens, 3500)
            print(f"Setting max_tokens to: {max_output_tokens}")

            # Use the Messages API format with adjusted token limit
            response = anthropic_client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=max_output_tokens,
                messages=[
                    {
                        "role": "user",
                        "content": formatted_prompt
                    }
                ]
            )
            
            # Extract content from the response
            raw_content = response.content[0].text
            print(f"Raw content:\n{raw_content}")
            print(f"Response type: {type(raw_content)}")

            # Extract title
            story = {'title': fallback_title_parser(raw_content)}
            
            # If fallback parser didn't find both titles, try original method
            if not story['title']['english'] or not story['title']['tetun']:
                try:
                    lines = str(raw_content).split('\n')
                    english_title = next((line.split('English')[1].strip('():') for line in lines if 'English' in line), '')
                except (IndexError, AttributeError):
                    pass
                
            # Split the content into parts
            parts = raw_content.split('\n\n')

            # Try multiple parsing methods in sequence
            story['parts'] = (
                parse_parts(raw_content) or 
                parse_parts_marker_based(parts) or 
                parse_parts_lark(parts) or 
                fallback_parse_parts(parts)
            )
        
            print(f"Parsed story structure: {json.dumps(story, indent=2)}")
            
            return story

        except anthropic.APIError as e:
            if 'Error code: 529' in str(e) and attempt < max_retries - 1:
                print(f"Encountered 529 error. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                raise
        except Exception as e:
            print(f"Unexpected error in generate_story: {str(e)}")
            print(f"Traceback: {traceback.format_exc()}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                raise

    raise Exception(f"Failed to generate story after {max_retries} attempts")
    
def generate_image(english_story_parts, part, style, part_number, is_first_image=False, additional_payload=None):
    story_instruction = f"Create a whimsical, child-friendly {style} illustration for a bedtime story. Generate the image for part {part_number}."
    consistency_prompt = "Create a consistent style for the story." if is_first_image else "Maintain style consistency with previous illustrations."
    full_story = " ".join(english_story_parts)
    style_prompt = """
    Use a vibrant, colorful palette reminiscent of Jaime Hernandez's work in Love and Rockets.
    Character designs should blend realistic proportions with slightly exaggerated features, similar to an anime style.
    Architecture should be gigantic, whimsical, ultra technical or magical or cosmic. Very comic book. 
    Flora and fauna should me mythical, magical, diverse and local to Nepal.
    Include details that reflect Nepalese culture, local flora and fauna, and the Divine Mother who nourishes all in this land.
    Mix ultra post-modern and ancient anachronistic elements to create a unique, futuristic Nepalese aesthetic.
    Use dynamic compositions and dramatic angles inspired by comic book panels.
    Incorporate subtle magical or fantastical elements that blend seamlessly with the realistic setting.
    Emphasize expressive character faces and body language to convey emotions.
    Use lighting effects to create mood and atmosphere, especially for scenes set at different times of day.    
    Use a vibrant, bold color palette with rich, saturated hues, particularly emphasizing warm oranges, deep teals, and lush greens.
    Employ a comic book or graphic novel art style with clean, defined outlines and flat colors.
    Create detailed, fantastical backgrounds that blend natural elements with cosmic imagery.
    Use perspective to create a sense of wonder, such as positioning the viewer to look up at towering flora or celestial objects.
    Incorporate small, whimsical details like floating particles or small creatures to add life to the scene.
    Ensure character clothing is simple yet modern, with solid colors that stand out against the busy background.
    Use subtle gradients and shading to add dimension to flat color areas, especially on larger objects.
    """
    story_part = "In Nepal: " + part
    
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "Accept": "image/*",
        "Authorization": f"Bearer {stability_api_key}"
    }
    
    # Base payload with corrected cfg_scale value
    payload = {
        "prompt": (None, story_instruction + " " + story_part + " " + style_prompt + " " + consistency_prompt),
        "negative_prompt": (None, ""),
        "output_format": (None, "png"),
        "cfg_scale": (None, "7"),  # Reduced from 15 to 7
        "clip_guidance_preset": (None, "SLOWEST"),
        "height": (None, "576"),
        "width": (None, "1024"),
        "samples": (None, "1"),
        "steps": (None, "50"),
        "style_preset": (None, style),
        "model": (None, "sd3-large"),
        "seed": (None, "3994967295")
    }

    # Update payload with additional parameters if provided
    if additional_payload:
        for key, value in additional_payload.items():
            payload[key] = (None, str(value))

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
                content = e.response.content.decode('utf-8') if e.response else "No response content"
                print(f"Decoded response: {content}")
            
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise

    print('Image generation failure after all attempts')
    return None
    
def download_image_from_s3(image_url):
    bucket_name = 'tl-web'
    key = image_url.split('tl-web/')[-1]  # Extract the key from the URL
    local_path = '/tmp/image.png'  # Use /tmp for Lambda's writable directory
    s3.download_file(bucket_name, key, local_path)
    return local_path

def load_story_prompt():
    with open('story_prompt.txt', 'r') as file:
        return file.read()
        
def lambda_handler(event, context):
    # Safely get headers and origin with proper defaults
    headers = event.get('headers', {}) or {}
    origin = headers.get('origin', headers.get('Origin', ''))
    
    # Define CORS headers based on allowed origins
    cors_headers = {
        'Access-Control-Allow-Origin': origin if origin in ALLOWED_ORIGINS else ALLOWED_ORIGINS[0],
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST'
    }

    print("Full event:", event)
    
    # Determine if this is a test event and format the body accordingly
    if isinstance(event, dict):
        is_test_event = 'key1' in event or 'story_seed' in event
        if is_test_event:
            print("Detected test event")
            method = 'POST'
            # Use event directly as body for test events
            body = event
        else:
            # Handle API Gateway events
            method = (
                event.get('requestContext', {}).get('http', {}).get('method') or
                event.get('requestContext', {}).get('httpMethod') or
                event.get('httpMethod')
            )
            try:
                body = json.loads(event.get('body', '{}'))
            except json.JSONDecodeError:
                body = {}
    else:
        method = 'POST'
        body = {'story_seed': ''}

    print("Detected method:", method)
    print("Parsed body:", body)

    # Handle CORS preflight request
    if method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': cors_headers
        }

    # Handle POST request (including test events)
    if method == 'POST':
        try:
            # For test events, use default values if not provided
            if is_test_event:
                provided_seed = body.get('story_seed', body.get('key1', ''))
                # For test events, bypass password check
                password = ALLOWED_PASSWORDS[0] if ALLOWED_PASSWORDS else ''
            else:
                provided_seed = body.get('story_seed', '')
                password = body.get('password', '')

            # Skip password check for test events
            if not is_test_event and password not in ALLOWED_PASSWORDS:
                return {
                    'statusCode': 403,
                    'headers': {**cors_headers, 'Content-Type': 'application/json'},
                    'body': json.dumps({'message': 'Invalid password'})
                }

            print('story_seed:', provided_seed)
            
            max_retries = 3
            retry_count = 0
            last_error = None

            while retry_count < max_retries:
                try:
                    # Load necessary files and setup
                    seed_file = load_random_file()
                    story_prompt = load_story_prompt()
                    random_elements = load_random_elements()

                    # Determine story seed
                    story_seed = provided_seed if provided_seed and len(provided_seed) > 15 else random.choice(random_elements)

                    # Generate the story
                    story = generate_story(seed_file, story_prompt, story_seed)

                    # Validate story content
                    english_title = story['title']['english']
                    english_story_parts = [part['english'] for part in story['parts']]

                    if not english_title or not english_story_parts:
                        raise ValueError("Generated story is incomplete")

                    # Generate safe title for filenames
                    safe_title = ''.join(c if c.isalnum() else '_' for c in english_title.lower())
                    date_str = datetime.now().strftime("%Y%m%d")

                    # Setup art style
                    styles = ['comic-book', 'digital-art', 'fantasy-art', 'tile-texture']
                    style = random.choices(styles, weights=[2, 3, 2, 1])[0]
                    print(f"Selected style: {style}")

                    # Generate images and sounds
                    image_urls = []
                    sound_urls = []
                    first_image = None

                    for i, part in enumerate(english_story_parts, 1):
                        # Image generation with retries
                        image = None
                        for image_attempt in range(3):
                            try:
                                is_first_image = (i == 1)
                                additional_payload = None
                                
                                if i > 1 and first_image is not None:
                                    additional_payload = {
                                        "init_image": base64.b64encode(first_image.getvalue()).decode('utf-8'),
                                        "init_image_mode": "IMAGE_STRENGTH",
                                        "image_strength": 0.35
                                    }
                                
                                image = generate_image(
                                    english_story_parts, 
                                    part, 
                                    style, 
                                    part_number=i,
                                    is_first_image=is_first_image,
                                    additional_payload=additional_payload
                                )
                                
                                if image is not None:
                                    if i == 1:
                                        first_image = image
                                    break
                                    
                            except Exception as img_error:
                                print(f"Image generation attempt {image_attempt + 1} for part {i} failed: {str(img_error)}")
                                if image_attempt < 2:
                                    time.sleep(2)

                        if image is None:
                            raise Exception(f"Failed to generate image for part {i}")

                        # Save image and generate sound
                        image_name = f'{safe_title}_image_{i}_{date_str}.png'
                        image_url = save_image_to_s3(image, image_name)
                        image_urls.append(f"https://tl-web.s3.us-west-2.amazonaws.com/{image_url}")

                        sound_filename = f'{safe_title}_sound_{i}_{date_str}.mp3'
                        sound_url = generate_sound(part, sound_filename)
                        sound_urls.append(sound_url)

                    # Generate and save HTML
                    html_content = generate_html(story, image_urls, sound_urls)
                    new_html_key = f'stories/bedtime_{safe_title}_{int(time.time())}.html'

                    s3.put_object(
                        Bucket='tl-web',
                        Key=new_html_key,
                        Body=html_content,
                        ContentType='text/html'
                    )

                    # Update image gallery and return success
                    generate_image_gallery()
                    return {
                        'statusCode': 200,
                        'headers': {**cors_headers, 'Content-Type': 'application/json'},
                        'body': json.dumps({
                            'message': f"Bedtime story '{english_title}' with {len(english_story_parts)} parts generated and saved to s3://tl-web/{new_html_key}."
                        })
                    }

                except Exception as e:
                    last_error = e
                    retry_count += 1
                    print(f"Attempt {retry_count} failed: {str(e)}")
                    print(f"Traceback: {traceback.format_exc()}")
                    if retry_count < max_retries:
                        print(f"Retrying... ({retry_count}/{max_retries})")
                        time.sleep(2 ** retry_count)
                    else:
                        break

            # If we've exhausted all retries, return error response
            return {
                'statusCode': 500,
                'headers': {**cors_headers, 'Content-Type': 'application/json'},
                'body': json.dumps({
                    'error': f"Failed after {max_retries} attempts",
                    'details': str(last_error),
                    'traceback': traceback.format_exc()
                })
            }

        except Exception as e:
            return {
                'statusCode': 500,
                'headers': {**cors_headers, 'Content-Type': 'application/json'},
                'body': json.dumps({
                    'error': 'Unexpected error',
                    'details': str(e),
                    'traceback': traceback.format_exc()
                })
            }

    # If method is not detected or neither OPTIONS nor POST
    print("Method not allowed:", method)
    return {
        'statusCode': 405,
        'headers': {**cors_headers, 'Content-Type': 'application/json'},
        'body': json.dumps({
            'error': 'Method not allowed',
            'method': method,
            'event_structure': str(event),
            'is_test': is_test_event if 'is_test_event' in locals() else False
        })
    }