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

# Set up paths (assuming the script is in the same directory as the JSON files)
SCRIPT_DIR = Path(__file__).resolve().parent
DICT_FILE = SCRIPT_DIR / 'dictionary.json'
PHRASES_FILE = SCRIPT_DIR / 'phrases.json'
COMPOUND_FILE = SCRIPT_DIR / 'compound.json'
RANDOM_ELEMENTS_FILE = SCRIPT_DIR / 'random_elements.json'

TIMOR_LESTE_CULTURES = [
    {"people": "Tetum"},
    {"people": "Mambae"},
    {"people": "Tukudede"},
    {"people": "Galoli"},
    {"people": "Kemak"},
    {"people": "Baikeno"},
    {"people": "Timor Leste Muslim"},
    {"people": "Timor Leste Chinese"}
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

english_to_tetun = load_dict_file(DICT_FILE)
tetun_phrases = load_dict_file(PHRASES_FILE)
tetun_compounds = load_dict_file(COMPOUND_FILE)

# Initialize clients
anthropic_client = Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
s3 = boto3.client('s3')
stability_api_key = os.environ['STABILITY_API_KEY']

def load_random_file():
    s3_object = s3.get_object(Bucket='tl-web', Key='files.json')
    files_data = json.loads(s3_object['Body'].read().decode('utf-8'))
    random_file = random.choice(files_data['files'])
    return random_file['path']
        
def save_image_to_s3(image_data, image_name):
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
    
def generate_story(seed_file, story_prompt_template):
    max_retries = 3
    retry_delay = 5  # seconds

    for attempt in range(max_retries):
        try:
            selected_culture = random.choice([culture['people'] for culture in TIMOR_LESTE_CULTURES])
            
            # Load dictionary contents
            with open(DICT_FILE, 'r', encoding='utf-8') as f:
                dictionary_content = f.read()
            with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
                phrases_content = f.read()
            with open(COMPOUND_FILE, 'r', encoding='utf-8') as f:
                compound_content = f.read()
                
            # Load random elements
            random_elements = load_random_elements()
            story_seed = random.choice(random_elements)
            
            # Format the prompt template
            prompt = story_prompt_template.format(
                seed_file=seed_file,
                selected_culture=selected_culture,
                story_seed=story_seed,
                dictionary_content=dictionary_content,
                phrases_content=phrases_content,
                compound_content=compound_content
            )

            response = anthropic_client.completions.create(
                prompt=prompt,
                model="claude-v1",
                max_tokens_to_sample=7000,
                stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
            )
            
            raw_content = response.completion.strip()
            print(f"Raw content:\n{raw_content}")  # Debug print
            print(type(raw_content))

            # Extract title
            story = {'title': fallback_title_parser(raw_content)}
            
            # If fallback parser didn't find both titles, try original method
            if not story['title']['english'] or not story['title']['tetun']:
                try:
                    lines = str(raw_content).split('\n')
                    english_title = next((line.split('English')[1].strip('():') for line in lines if 'English' in line), '')
                    tetun_title = next((line.split('Tetun')[1].strip('():') for line in lines if 'Tetun' in line), '')
                    if english_title and tetun_title:
                        story['title'] = {'english': english_title, 'tetun': tetun_title}
                except (IndexError, AttributeError):
                    pass
                
            # Split the content into parts
            parts = raw_content.split('\n\n')

            story['parts'] = parse_parts(raw_content)
            
            if not story['parts']:
                story['parts'] = parse_parts_marker_based(parts)
            
            if not story['parts']:
                story['parts'] = parse_parts_lark(parts)
            
            if not story['parts']:
                story['parts'] = fallback_parse_parts(parts)
        
            print(f"Parsed story structure: {json.dumps(story, indent=2)}")  # Debug print
            
            return story, selected_culture 

        except anthropic.InternalServerError as e:
            if 'Error code: 529' in str(e) and attempt < max_retries - 1:
                print(f"Encountered 529 error. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                raise

    raise Exception(f"Failed to generate story after {max_retries} attempts due to server overload.")
    
def generate_image(english_story_parts, part, style, culture, part_number, is_first_image=False, additional_payload=None):
    story_instruction = f"Create a whimsical, child-friendly {style} illustration for a bedtime story. Generate the image for part {part_number}."

    culture_prompt = f"Make sure all people depicted look like {culture} people from Timor Leste. They should not be caucasian."
    
    consistency_prompt = "Create a consistent style for the story." if is_first_image else "Maintain style consistency with previous illustrations."
    full_story = " ".join(english_story_parts)
    
    style_prompt = """
    Use a vibrant, colorful palette reminiscent of Jaime Hernandez's work in Love and Rockets.
    Character designs should blend realistic proportions with slightly exaggerated features, similar to Wendy Pini's elves in Elfquest.
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
    url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {stability_api_key}"
    }
    
    payload = {
        "text_prompts": [
            {"text": story_instruction, "weight": 1},
            {"text": part, "weight": 1.2},
            {"text": full_story[:1999], "weight": 0.75},
            {"text": culture_prompt, "weight": 0.75},
            {"text": style_prompt, "weight":1.5},
            {"text": consistency_prompt, "weight": 1},
        ],
        "cfg_scale": 15,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 576,
        "width": 1024,
        "samples": 1,
        "steps": 50,
        "style_preset": style,
        "seed": 3994967295
    }

    # Update payload with additional parameters if provided
    if additional_payload:
        payload.update(additional_payload)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}: Sending request with payload: {json.dumps(payload, indent=2)}")
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            
            data = response.json()
            if "artifacts" in data and len(data["artifacts"]) > 0:
                image_data = base64.b64decode(data["artifacts"][0]["base64"])
                return BytesIO(image_data)
            else:
                error_message = data.get("message", "Unknown error occurred")
                raise Exception(f"No image data in response. Error: {error_message}")
        except requests.exceptions.RequestException as e:
            print(f"Error generating image on attempt {attempt + 1}: {str(e)}")
            if e.response is not None:
                print(f"Response content: {e.response.content}")
            
            if attempt < max_retries - 1:
                print(f"Retrying in 2 seconds...")
                time.sleep(2)  # Wait for 2 seconds before retrying
            else:
                raise
        
        # Add a pause between attempts to handle rate limiting
        if attempt < max_retries - 1:
            time.sleep(1)  # 1 second pause between attempts
    print('Image generation failure')
    sys.exit()

    
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
    max_retries = 3
    for attempt in range(max_retries):
        try:
            seed_file = load_random_file()
            story_prompt = load_story_prompt()

            story, selected_culture = generate_story(seed_file, story_prompt)
            
            english_title = story['title']['english']
            tetun_title = story['title']['tetun']
            
            english_story_parts = [part['english'] for part in story['parts']]
            tetun_story_parts = [part['tetun'] for part in story['parts']]
            
            if not english_title or not tetun_title or len(english_story_parts) == 0 or len(tetun_story_parts) == 0:
                print(f"Attempt {attempt + 1}: Generated story is incomplete.")
                print(f"English title: {english_title}")
                print(f"Tetun title: {tetun_title}")
                print(f"Number of English parts: {len(english_story_parts)}")
                print(f"Number of Tetun parts: {len(tetun_story_parts)}")
                continue
            
            safe_title = ''.join(c if c.isalnum() else '_' for c in english_title.lower())
            date_str = datetime.now().strftime("%Y%m%d")
            
            styles = ['anime', 'comic-book', 'digital-art', 'enhance', 'fantasy-art', 'isometric', 'line-art', 'modeling-compound', 'neon-punk', 'tile-texture']
            random.shuffle(styles)
            weights = [random.randint(1, 3) for _ in range(len(styles))]
            
            style = random.choices(styles, weights=weights)[0]
            print(f"Selected style: {style}")
            
            image_urls = []
            sound_urls = []
            for i, part in enumerate(english_story_parts, 1):
                # Generate image
                image = None
                for image_attempt in range(3):
                    try:
                        is_first_image = (i == 1)
                        image = generate_image(english_story_parts, part, style, selected_culture, part_number=i, is_first_image=is_first_image)
                        if image is not None:
                            break
                    except Exception as img_error:
                        print(f"Image generation attempt {image_attempt + 1} for part {i} failed: {str(img_error)}")
                        if image_attempt < 2:
                            time.sleep(2)
                        continue
            
                if image is not None:
                    image_name = f'{safe_title}_image_{i}_{date_str}.png'
                    image_url = save_image_to_s3(image, image_name)
                    image_urls.append(image_url)
                    
                    # Store the first generated image
                    if i == 1:
                        first_image = image
                        
                    # Update the payload with the first image for subsequent generations
                    if i > 1 and first_image is not None:
                        payload = {
                            "init_image": base64.b64encode(first_image.getvalue()).decode('utf-8'),
                            "init_image_mode": "IMAGE_STRENGTH",
                            "image_strength": 0.35
                        }
                        # Update the generate_image function call to include the payload
                        image = generate_image(english_story_parts, part, style, selected_culture, part_number=i, is_first_image=False, additional_payload=payload)
                else:
                    print(f"Failed to generate image for part {i} after 3 attempts.")
                    raise Exception(f"Failed to generate image for part {i}")

                # Generate sound
                sound_filename = f'{safe_title}_sound_{i}_{date_str}.mp3'
                sound_url = generate_sound(part, sound_filename)
                sound_urls.append(sound_url)

            # Check if we have the correct number of images and sounds
            if len(image_urls) != len(english_story_parts) or len(sound_urls) != len(english_story_parts):
                raise Exception(f"Mismatch between number of story parts ({len(english_story_parts)}) and generated media (images: {len(image_urls)}, sounds: {len(sound_urls)})")

            html_content = generate_html(story, image_urls, sound_urls)
            
            try:
                old_html = s3.get_object(Bucket='tl-web', Key='bedtime.html')['Body'].read().decode('utf-8')
                old_html = old_html.replace('images/', '../images/')
                old_html_key = f'stories/bedtime_{int(time.time())}.html'
                s3.put_object(
                    Bucket='tl-web',
                    Key=old_html_key,
                    Body=old_html,
                    ContentType='text/html'
                )
                print(f"Old story saved to {old_html_key}")
            except s3.exceptions.NoSuchKey:
                print("No previous bedtime.html found. Skipping copy.")
            
            s3.put_object(
                Bucket='tl-web',
                Key='bedtime.html',
                Body=html_content,
                ContentType='text/html'
            )
            
            generate_image_gallery()
            return {
                'statusCode': 200,
                'body': json.dumps(f"Bedtime story '{english_title}' for {selected_culture} culture with {len(english_story_parts)} parts generated and saved to s3://tl-web/bedtime.html. Previous story archived.")
            }
        
        except Exception as e:
            print(f"Attempt {attempt + 1} failed. Error: {str(e)}")
            print(f"Full error traceback: {traceback.format_exc()}")
            if attempt == max_retries - 1:
                return {
                    'statusCode': 500,
                    'body': json.dumps({
                        "error": f"An error occurred after {max_retries} attempts",
                        "details": str(e),
                        "traceback": traceback.format_exc()
                    })
                }
            else:
                print(f"Retrying entire process. Attempt {attempt + 2} of {max_retries}")
                continue

    return {
        'statusCode': 500,
        'body': json.dumps("Failed to generate a valid story with all images after multiple attempts.")
    }