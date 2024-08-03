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

def generate_html(title, story_parts, image_urls, tetun_title, tetun_story_parts):
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
            .tetun {{ font-style: italic; color: #666; }}
        </style>
    </head>
    <body>
        <h1>{tetun_title}</h1>
        <h1>{title}</h1>
    """
    
    for i, (eng_part, tetun_part, image_url) in enumerate(zip(story_parts, tetun_story_parts, image_urls), 1):
        html += f"""
        <div class="story-part">
            <p>{eng_part}</p>
            <p class="tetun">{tetun_part}</p>
            <img src="{image_url}" alt="Story illustration {i}">
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
    
    
def generate_story(seed_file):
    # Load dictionary contents
    with open(DICT_FILE, 'r', encoding='utf-8') as f:
        dictionary_content = f.read()
    with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
        phrases_content = f.read()
    with open(COMPOUND_FILE, 'r', encoding='utf-8') as f:
        compound_content = f.read()

    prompt = f"""Human: Based on the file '{seed_file}', create a bedtime story for children of Timor Leste from a non-dual, spiritual perspective that emphasizes the interconnectedness of all life and encourages living in loving harmony with mother nature. The story should be suitable for young children and have a clear beginning, middle, and end. Please provide the story in three parts, each around 100 words long. Also, provide a short title for the story.

    After generating the story in English, translate it to Tetun. When translating, please consider the following Tetun grammar rules:
    
    1. Word order: In Tetun, the verb often comes at the end of the sentence. If a sentence has 3 or more words and doesn't start with a pronoun (Hau, O, Nia, Ita, Ami, Imi, Sira), move the first word to the end of the sentence.
    
    2. Aspect markers: Use the following Tetun words:
       - 'ona' for completed actions (e.g., "Hau han ona" = "I have eaten")
       - 'tiha' for perfective aspect (e.g., "Hau han tiha" = "I ate")
       - 'hela' for continuous actions (e.g., "Hau han hela" = "I am eating")
       - 'sei' for future actions (e.g., "Hau sei han" = "I will eat")
    
    3. Pronouns: Use the following Tetun pronouns:
       - 'Hau' for 'I'
       - 'O' for 'you' (informal)
       - 'Ita' for 'you' (formal) or 'we' (inclusive)
       - 'Nia' for 'he/she/it'
       - 'Ami' for 'we' (exclusive)
       - 'Imi' for 'you' (plural)
       - 'Sira' for 'they'
    
    4. Use the possessive marker 'nia' between the possessor and the possessed item (e.g., "Maria nia uma" = "Maria's house")
    
    5. Use 'mak' for focus or emphasis (e.g., "Maria mak han" = "It was Maria who ate")
    
    6. Use 'katak' to introduce reported speech or thoughts (e.g., "Nia dehan katak..." = "He said that...")
    
    Use the provided dictionaries to assist with the translation:
    
    Dictionary: {dictionary_content}
    Phrases: {phrases_content}
    Compound words: {compound_content}
    
    Please provide a full translation but use the Dictionary to help you with words you don't know in Tetum.
    
    Return the story in the following format without any additional text:
    Title (English): [English Title]
    Title (Tetun): [Tetun Title]

    Part 1 (English): [English text for Part 1]
    Part 1 (Tetun): [Tetun translation for Part 1]

    Part 2 (English): [English text for Part 2]
    Part 2 (Tetun): [Tetun translation for Part 2]

    Part 3 (English): [English text for Part 3]
    Part 3 (Tetun): [Tetun translation for Part 3]

    Human: Generate the story as described above, following the exact format specified.

    Assistant: Title (English): [English Title]
    Title (Tetun): [Tetun Title]

    Part 1 (English): [English text for Part 1]
    Part 1 (Tetun): [Tetun translation for Part 1]

    Part 2 (English): [English text for Part 2]
    Part 2 (Tetun): [Tetun translation for Part 2]

    Part 3 (English): [English text for Part 3]
    Part 3 (Tetun): [Tetun translation for Part 3]

    Human: Thank you for generating the story. Please return this output exactly as is, with no additional text.

    Assistant: Title (English): [English Title]
    Title (Tetun): [Tetun Title]

    Part 1 (English): [English text for Part 1]
    Part 1 (Tetun): [Tetun translation for Part 1]

    Part 2 (English): [English text for Part 2]
    Part 2 (Tetun): [Tetun translation for Part 2]

    Part 3 (English): [English text for Part 3]
    Part 3 (Tetun): [Tetun translation for Part 3]
    Assistant:"""

    response = anthropic_client.completions.create(
        prompt=prompt,
        model="claude-v1",
        max_tokens_to_sample=2000,
        stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
    )
    
    story_content = response.completion.strip().split('\n\n')
    
    # Remove any introductory lines
    while story_content and not story_content[0].startswith("Title"):
        story_content.pop(0)
    
    # Add debugging information
    print(f"Generated story content (first 500 characters): {story_content[:500]}")
    print(f"Number of story parts: {len(story_content)}")
    
    # Ensure we have the correct number of parts
    if len(story_content) != 4:  # Title + 3 parts
        raise ValueError(f"Incorrect number of story parts. Expected 4, got {len(story_content)}. Content: {story_content}")
    
    return story_content

def lambda_handler(event, context):
    try:
        seed_file = load_random_file()
        story_content = generate_story(seed_file)
        
        # Parse the title
        title_parts = story_content[0].split('\n')
        english_title = title_parts[0].replace("Title (English): ", "").strip()
        tetun_title = title_parts[1].replace("Title (Tetun): ", "").strip()
        
        english_story_parts = []
        tetun_story_parts = []
        
        for part in story_content[1:]:
            part_lines = part.split('\n')
            english_story_parts.append(part_lines[0].replace("Part 1 (English): ", "").strip())
            tetun_story_parts.append(part_lines[1].replace("Part 1 (Tetun): ", "").strip())
        
        safe_title = ''.join(c if c.isalnum() else '_' for c in english_title.lower())
        date_str = datetime.now().strftime("%Y%m%d")
        
        image_urls = []
        for i, part in enumerate(english_story_parts, 1):
            image = generate_image(part[:100])
            image_name = f'{safe_title}_image_{i}_{date_str}.png'
            image_url = save_image_to_s3(image, image_name)
            image_urls.append(image_url)
        
        html_content = generate_html(english_title, english_story_parts, image_urls, tetun_title, tetun_story_parts)
        
        s3.put_object(
            Bucket='tl-web',
            Key='bedtime.html',
            Body=html_content,
            ContentType='text/html'
        )
        generate_image_gallery()
        return {
            'statusCode': 200,
            'body': json.dumps(f"Bedtime story '{english_title}' generated and saved to s3://tl-web/bedtime.html")
        }
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"An error occurred: {str(e)}")
        }