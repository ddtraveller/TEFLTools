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
from random import choice
import colorsys
import time
import traceback
from lark import Lark, Transformer
from gtts import gTTS
import sys

# Set up paths (assuming the script is in the same directory as the JSON files)
SCRIPT_DIR = Path(__file__).resolve().parent
DICT_FILE = SCRIPT_DIR / 'dictionary.json'
PHRASES_FILE = SCRIPT_DIR / 'phrases.json'
COMPOUND_FILE = SCRIPT_DIR / 'compound.json'

TIMOR_LESTE_CULTURES = [
    {"people": "Tetum"},
    {"people": "Mambae"},
    {"people": "Tukudede"},
    {"people": "Galoli"},
    {"people": "Kemak"},
    {"people": "Baikeno"}
]

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
    
    for i, (part, image_url, sound_url) in enumerate(zip(story['parts'], image_urls, sound_urls), 1):
        english_text = re.sub(r'Part \d+$', '', part['english']).strip()
        html += f"""
        <div class="story-part">
            <h2>Part {i}</h2>
            <p>{english_text}</p>
            <p class="tetun">{part['tetun']}</p>
            <img src="{image_url}" alt="Story illustration {i}">
            <audio controls>
                <source src="{sound_url}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
        </div>
        """
    
    html += """
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
    part_markers = ['Part 1', 'Part 2', 'Part 3', 'Part 4', 'Part 5']
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
        if english_title and tetun_title:
            break
    
    return {'english': english_title, 'tetun': tetun_title}
    
def generate_story(seed_file, story_prompt_template):
    try:
        selected_culture = random.choice([culture['people'] for culture in TIMOR_LESTE_CULTURES])
        
        # Load dictionary contents
        with open(DICT_FILE, 'r', encoding='utf-8') as f:
            dictionary_content = f.read()
        with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
            phrases_content = f.read()
        with open(COMPOUND_FILE, 'r', encoding='utf-8') as f:
            compound_content = f.read()

        # Reintroducing the random story seeds
        random_elements = [
            "Include a magical creature unique to this story",
            "Show a fantastic landscape inspired by Timor-Leste's geography",
            "Depict a heartwarming moment between characters",
            "Illustrate a surprising discovery in an unexpected place",
            "Present a whimsical character with a unique appearance",
            "Portray a wise elder sharing knowledge under a sacred tree",
            "Show a mythical beast soaring through misty mountains",
            "Depict a common animal transforming into a legendary creature",
            "Illustrate a trickster figure wielding a magical artifact",
            "Present a symbol of rebirth emerging from adversity",
            "Show a group of animals displaying human-like behavior",
            "Depict a celestial being performing a mundane task",
            "Illustrate star-crossed lovers overcoming an otherworldly obstacle",
            "Show two opposing forces in harmonious balance",
            "Present a child receiving wisdom from an ancient being",
            "Depict a supernatural entity emerging from a natural feature",
            "Show a humble villager discovering a hidden realm",
            "Illustrate a common object granting an extraordinary ability",
            "Present a hero receiving a divinely-inspired tool",
            "Depict a benevolent spirit helping a lost traveler",
            "Show children's toys coming to life in a playful manner",
            "Illustrate a wise animal teaching young ones an important lesson",
            "Present a creature overcoming a great challenge to achieve transformation",
            "Depict a child befriending a gentle, misunderstood beast",
            "Show an animal guardian protecting a sacred object",
            "Illustrate a farmer discovering an extraordinary being in their field",
            "Present animals holding a formal human-like gathering",
            "Depict an artist's creation magically coming to life",
            "Show a child learning a life lesson from industrious insects",
            "Illustrate a mythical being crafting celestial objects",
            "Present inanimate objects becoming animated at night",
            "Depict a musical instrument with the power to affect nature",
            "Show a child's imagination bringing shadows to life",
            "Illustrate an ancient tree sharing knowledge with a listener",
            "Present grateful spirits honoring a kind-hearted person",
            "Depict a small, brave animal defending its community",
            "Show a legendary weapon choosing its destined wielder",
            "Illustrate a child learning to harness a natural element",
            "Present celestial beings interacting with humans in a festival",
            "Depict a magical object granting wishes with unexpected results",
            "Show a child receiving training in traditional skills from mystical mentors",
            "Illustrate a tiny, luminous insect guiding travelers through darkness",
            "Present an artifact that can influence the environment",
            "Depict a child learning stealth from a Timor-Leste native animal",
            "Show small creatures working together to accomplish a great task",
            "Illustrate a miniature world contained within a common object",
            "Present a child gaining insight from a river or mountain spirit",
            "Depict a mystical object revealing hidden truths",
            "Show everyday tools working autonomously to complete a task",
            "Illustrate a child discovering the ability to communicate with nature",
            "Present an enchanted object revealing one's true path",
            "Depict a Timorese firefly leading lost souls to safety",
            "Show a child learning bravery from a small but courageous animal",
            "Illustrate a traditional Timorese object granting the power of flight",
            "Present guardian spirits awakening to protect their charges"
        ]

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
            max_tokens_to_sample=5000,
            stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
        )
        
        raw_content = response.completion.strip()
        print(f"Raw content:\n{raw_content}")  # Debug print
        print(type(raw_content))

        # Extract title
        try:
            english_title = str(raw_content).split('\n')[0].split('English')[1].split('\n')[0].strip('():')
            tetun_title = str(raw_content).split('\n')[1].split('Tetun')[1].split('\n')[0].strip('():')
            story = {
                'title': {'english': english_title, 'tetun': tetun_title}
            }
        except (IndexError, AttributeError):
            # If the original method fails, use the fallback parser
            story = {'title': fallback_title_parser(raw_content)}
            
        # Split the content into parts
        parts = raw_content.split('\n\n')

        story['parts'] = parse_parts_marker_based(parts)
        
        try: 
            story['parts']
        except:
            story['parts'] = parse_parts_lark(parts)
        
        try: 
            story['parts']
        except:            
            story['parts'] = fallback_parse_parts(parts)

        print(f"Parsed story structure: {json.dumps(story, indent=2)}")  # Debug print
        
        return story, selected_culture 

    except Exception as e:
        print(f"Error in generate_story: {str(e)}")
        print(f"Traceback: {traceback.format_exc()}")
        raise
    
def generate_image(english_story_parts, prompt, style, culture, custom_style, part_number=1):
    story_context = f"Create a whimsical, child-friendly {style} illustration for the following bedtime story: {english_story_parts}.\nGenerate the image for part {part_number} in the story: {prompt}."
    
    story_context += f' Make sure all people depicted look like {culture} people.'

    if part_number > 1:
        story_context += f" Maintain style consistency with previous illustrations."

    url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {stability_api_key}"
    }
    
    # Load cfg_scale and steps from the Lambda configuration
    cfg_scale = float(os.environ.get('CFG_SCALE', 14))
    steps = int(os.environ.get('STEPS', 40))    
    
    payload = {
        "text_prompts": [
            {"text": story_context, "weight": 1}
        ],
        "cfg_scale": cfg_scale,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 576,
        "width": 1024,
        "samples": 1,
        "steps": steps,
        "style_preset": style,
        "seed": random.randint(0, 4294967295)
    }
    
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
                print(f"No image data in response: {json.dumps(data, indent=2)}")
                
                # Check for content filtering
                if "message" in data and "safety" in data["message"].lower():
                    print("Content filtering detected. Adjusting prompt...")
                    # Modify the prompt to be more child-friendly
                    story_context = f"Create a very mild, child-safe {style} illustration for a bedtime story. {prompt}"
                    payload["text_prompts"][0]["text"] = story_context
                else:
                    print('Image generation failure')
                    sys.exit()
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
    max_retries = 1
    for attempt in range(max_retries):
        try:
            seed_file = load_random_file()
            # Load the prompt from the text file
            story_prompt = load_story_prompt()

            story = {'parts': []}
            while len(story['parts']) < 3:
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
            
            # Choose a single style for the entire story
            styles = ['analog-film', 'anime', 'cinematic', 'comic-book', 'digital-art', 'enhance', 'fantasy-art', 'isometric', 'line-art', 'modeling-compound', 'neon-punk', 'origami', 'photographic', 'pixel-art', 'tile-texture']
            random.shuffle(styles)
            weights = [random.randint(1, 3) for _ in range(len(styles))]
            
            style = random.choices(styles, weights=weights)[0]
            print(f"Selected style: {style}")
            
            # Create a custom style description
            custom_style = f" Maintain a consistent art style across all illustrations. "

            image_urls = []
            for i, part in enumerate(english_story_parts, 1):
                image = None
                for image_attempt in range(2):  # 0 for first attempt, 1 for retry
                    try:
                        prompt = part[:300] if image_attempt == 0 else part[:400]
                        image = generate_image(english_story_parts, prompt, style, selected_culture, custom_style, part_number=i)
                        if image is not None:
                            break
                    except Exception as img_error:
                        print(f"Image generation attempt {image_attempt + 1} for part {i} failed: {str(img_error)}")
                        if image_attempt == 0:
                            time.sleep(2)  # Wait for 2 seconds before retrying
                        continue

                if image is not None:
                    image_name = f'{safe_title}_image_{i}_{date_str}.png'
                    image_url = save_image_to_s3(image, image_name)
                    image_urls.append(image_url)
                else:
                    raise Exception(f"Failed to generate image for part {i} after 2 attempts")

            # If we've made it here, all images were generated successfully
            
            sound_urls = []
            for i, part in enumerate(english_story_parts, 1):
                sound_filename = f'{safe_title}_sound_{i}_{date_str}.mp3'
                sound_url = generate_sound(part, sound_filename)
                sound_urls.append(sound_url)

            html_content = generate_html(story, image_urls, sound_urls)
            
            # Copy the old bedtime.html to stories folder with updated name
            try:
                old_html = s3.get_object(Bucket='tl-web', Key='bedtime.html')['Body'].read().decode('utf-8')
                
                # Update image links in the old HTML
                old_html = old_html.replace('images/', '../images/')
                
                # Save the old HTML to the stories folder
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
            
            # Save the new HTML content
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

    # This line should never be reached, but just in case:
    return {
        'statusCode': 500,
        'body': json.dumps("Failed to generate a valid story after multiple attempts.")
    }