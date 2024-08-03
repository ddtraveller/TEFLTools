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

# Set up paths (assuming the script is in the same directory as the JSON files)
SCRIPT_DIR = Path(__file__).resolve().parent
DICT_FILE = SCRIPT_DIR / 'dictionary.json'
PHRASES_FILE = SCRIPT_DIR / 'phrases.json'
COMPOUND_FILE = SCRIPT_DIR / 'compound.json'

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

def generate_story(seed_file):
    prompt = f"""Human: Based on the file '{seed_file}', create bedtime story for children of Timor Leste from a non-dual, spiritual perspective that emphasizes the interconnectedness of all life and encourages living in loving harmony with mother nature. The story should be suitable for young children and have a clear beginning, middle, and end. Please provide the story in three parts, each around 100 words long. Also, provide a short title for the story. Return only the text of the title and story with no additional text or commentary before or after the output of the story. Do not include and text that is not a part of the story title. Assistant:"""

    response = anthropic_client.completions.create(
        prompt=prompt,
        model="claude-v1",
        max_tokens_to_sample=2000,
        stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
    )
    
    story_content = response.completion.strip().split('\n\n')
    title = story_content[0].replace("Title: ", "").strip()
    story_parts = story_content[1:]
    return title, story_parts

def generate_image(prompt):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {stability_api_key}"
    }
    
    body = {
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 30,
        "text_prompts": [{"text": prompt, "weight": 1}],
    }
    
    response = requests.post(url, headers=headers, json=body)
    
    if response.status_code == 200:
        data = response.json()
        image_data = base64.b64decode(data["artifacts"][0]["base64"])
        return BytesIO(image_data)
    else:
        raise Exception(f"Error generating image: {response.text}")

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

# Function to preprocess Tetun word order
def preprocess_tetun_word_order(text):
    words = text.split()  
    if len(words) >= 3 and words[0] not in ['Hau', 'O', 'Nia', 'Ita', 'Ami', 'Imi', 'Sira']:
        words = words[1:] + [words[0]]
    return ' '.join(words)

# Dictionary of Tetun aspect markers and their English equivalents
aspect_markers = {
    'ona': 'already',
    'tiha': 'completed',
    'hela': 'continuing',    
    'foin': 'just', 
    'sei': 'still/will'
}

# Function to translate Tetun aspect markers
def translate_aspect_markers(text):
    for marker, translation in aspect_markers.items():
        # Handle aspect markers with multiple translations (e.g., 'sei')
        if '/' in translation:
            translations = translation.split('/')
            replacement = translations[0]  # Use the first translation as the default
            # Replace the aspect marker with the appropriate translation based on context
            text = re.sub(r'\b' + re.escape(marker) + r'\b', lambda match: replacement, text)
        else:
            # Replace the aspect marker with the translation
            text = re.sub(r'\b' + re.escape(marker) + r'\b', translation, text)
    return text

# Dictionary of Tetun pronouns and their English equivalents
pronoun_map = {
    'Hau': 'I',
    'O': 'you (informal)',
    'Ita': 'you (formal)/we (inclusive)',
    'Nia': 'he/she/it',
    'Ami': 'we (exclusive)',
    'Imi': 'you (plural)',
    'Sira': 'they'
}

# Function to translate Tetun pronouns
def translate_pronouns(text):
    for tetun, english in pronoun_map.items():
        # Extract the English pronoun without the parentheses
        match = re.search(r"(.*?)\s*\(", english)
        if match:
            english_pronoun = match.group(1)
        else:
            english_pronoun = english
        # Replace the Tetun pronoun in the text
        text = re.sub(r'\b' + re.escape(tetun) + r'\b', english_pronoun, text)
    return text

# Function to translate Tetun compound words
def translate_compounds(text):
    for compound, translation in tetun_compounds.items():
        # Extract the Tetun compound word without the parentheses
        match = re.search(r"(.*?)\s*\(", translation)
        if match:
            tetun_word = match.group(1)
        else:
            tetun_word = translation
        # Replace the compound word in the text
        text = re.sub(r'\b' + re.escape(compound) + r'\b', tetun_word, text)
    return text
    
# Function to handle Tetun reduplication  
def handle_reduplication(text):
    words = text.split()
    for i, word in enumerate(words):
        if i > 0 and word == words[i-1]:
            words[i] = 'very ' + word
    return ' '.join(words)
    
# Function to preprocess text
def preprocess_text(text):
    text = preprocess_tetun_word_order(text)
    text = translate_aspect_markers(text)
    text = translate_pronouns(text)
    text = translate_compounds(text)  
    text = handle_reduplication(text)
    return text

# Main function to translate English to Tetun
def translate_english_to_tetun(text):
    print("Translating text with Anthropic model")
    
    # Preprocess and perform initial translation
    preprocessed_text = preprocess_text(text)
    
    # Prepare the prompt for the AI model
    prompt = f"Human: Translate the following English text to Tetun. Keep in mind Tetun grammar rules:\n\n{preprocessed_text}\n\nReturn only the text of the translation with no additional text or commentary before or after the output of the translation.\n\nTetun translation:\n\nAssistant:"
    response = anthropic_client.completions.create(
        prompt=prompt,
        model="claude-v1",
        max_tokens_to_sample=1000,
        stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
    )
    translation = response.completion.strip()
    return translation

def generate_html(title, story_parts, image_urls, tetum_title, tetum_story_parts):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
            h1 {{ color: #2c3e50; }}
            .story-part {{ margin-bottom: 20px; }}
            img {{ max-width: 100%; height: auto; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <h1>{tetum_title}</h1>
    """
    
    for i, (part, image_url) in enumerate(zip(tetum_story_parts, image_urls)):
        html += f"""
        <div class="story-part">
            <p>{part}</p>
            <img src="{image_url}" alt="Story illustration {i+1}">
        </div>
        """
    
    html += f"""
        <h1>{title}</h1>
    """
    
    for i, (part, image_url) in enumerate(zip(story_parts, image_urls)):
        html += f"""
        <div class="story-part">
            <p>{part}</p>
            <img src="{image_url}" alt="Story illustration {i+1}">
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
    
def lambda_handler(event, context):
    try:
        seed_file = load_random_file()
        title, story_parts = generate_story(seed_file)
        
        safe_title = ''.join(c if c.isalnum() else '_' for c in title.lower())
        date_str = datetime.now().strftime("%Y%m%d")
        
        image_urls = []
        for i, part in enumerate(story_parts, 1):
            image = generate_image(part[:100])
            image_name = f'{safe_title}_image_{i}_{date_str}.png'
            image_url = save_image_to_s3(image, image_name)
            image_urls.append(image_url)
        
        tetum_title = translate_english_to_tetun(title)
        tetum_story_parts = [translate_english_to_tetun(part) for part in story_parts]
        
        html_content = generate_html(title, story_parts, image_urls, tetum_title, tetum_story_parts)
        
        s3.put_object(
            Bucket='tl-web',
            Key='bedtime.html',
            Body=html_content,
            ContentType='text/html'
        )
        generate_image_gallery()
        return {
            'statusCode': 200,
            'body': json.dumps(f"Bedtime story '{title}' generated and saved to s3://tl-web/bedtime.html")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"An error occurred: {str(e)}")
        }