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

def generate_html(title, story_parts, image_urls, tetun_title, tetun_story_parts, video_url=None):
    background_color = generate_pastel_color()
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
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
        </style>
    </head>
    <body>
        <h1>{tetun_title}</h1>
        <h1>{title}</h1>
    """
    
    for i, (eng_part, tetun_part, image_url) in enumerate(zip(story_parts, tetun_story_parts, image_urls), 1):
        html += f"""
        <div class="story-part">
            <h2>Part {i}</h2>
            <p>{eng_part}</p>
            <p class="tetun">{tetun_part}</p>
            <img src="{image_url}" alt="Story illustration {i}">
        </div>
        """
    
    if video_url:
        html += f"""
        <div class="story-part">
            <h2>Story Video</h2>
            <video width="100%" controls>
                <source src="{video_url}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
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
    selected_culture = random.choice(TIMOR_LESTE_CULTURES)
    
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

    prompt = f"""Human: Based on the source seed; '{seed_file}', create a bedtime story of 900-1200 words long for children of the {selected_culture['people']} people in Timor-Leste. The story should be from a spiritual perspective that emphasizes a random one of the following; 
    - interconnectedness of all life 
    - living in loving harmony with mother nature
    - kindness
    - sharing
    - the wonderment and joy of being a child
    - the nature of consciousness
    - principles of permaculture
    - principles of holistic healing
    - acceptance of and healing from trauma
    - healing from the death of a loved one
    - how pride and stubbornness lead to a fall
    - being able to touch the divine through the spirit in all things
    - a random good quality
    - fun
    - adventure
    - curiosity
    - bravery
    
    Additionally, incorporate this element into your story: {story_seed}
    
    The story should be suitable for young children and have a clear beginning, middle, and end. Please provide the story in three or more parts, each around 300-400 words long. Also, provide a short title for the story.
    
    After generating the story in English, translate it to Tetun. When translating, please consider the grammar rules of Tetun.

    Use the provided dictionaries to assist with the translation:
    
    Dictionary: {dictionary_content}
    Phrases: {phrases_content}
    Compound words: {compound_content}
    
    Please provide a full translation but use the Dictionary to help you with words you don't know in Tetun.
    
    Return the story in the following format without any additional text or brackets:
    Title (English): English Title
    Title (Tetun): Tetun Title

    Part 1 (English): English text for Part 1
    Part 1 (Tetun): Tetun translation for Part 1

    Part 2 (English): English text for Part 2
    Part 2 (Tetun): Tetun translation for Part 2

    Part 3 (English): English text for Part 3
    Part 3 (Tetun): Tetun translation for Part 3

    [Continue with additional parts if necessary]

    Human: Generate the story as described above, following the exact format specified.

    Assistant: Title (English): English Title
    Title (Tetun): Tetun Title

    Part 1 (English): English text for Part 1
    Part 1 (Tetun): Tetun translation for Part 1

    Part 2 (English): English text for Part 2
    Part 2 (Tetun): Tetun translation for Part 2

    Part 3 (English): English text for Part 3
    Part 3 (Tetun): Tetun translation for Part 3

    [Additional parts if generated]

    Human: Thank you for generating the story. Please return this output exactly as is, with no additional text.

    Assistant:"""

    response = anthropic_client.completions.create(
        prompt=prompt,
        model="claude-v1",
        max_tokens_to_sample=5000,
        stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
    )
    
    story_content = response.completion.strip().split('\n\n')
    
    # Remove any introductory lines
    while story_content and not story_content[0].startswith("Title"):
        story_content.pop(0)
    
    # Add debugging information
    print(f"Generated story content (first 500 characters): {story_content[:500]}")
    print(f"Number of story parts: {len(story_content)}")
    
    # Ensure we have at least a title and one part
    if len(story_content) < 2:
        raise ValueError(f"Insufficient story parts. Expected at least 2, got {len(story_content)}. Content: {story_content}")
    
    return story_content, selected_culture 
    
def generate_image(prompt, style, culture, custom_style, part_number=1):
    story_context = f"Create a whimsical, child-friendly {style} illustration for the following part of a bedtime story set in Timor-Leste. Here is the story part; {prompt}. This is for part {part_number} of the story."
    cultural_context = f"Incorporate elements from {culture['people']} culture of Timor-Leste. "
    image_prompt = story_context + cultural_context + custom_style 

    if part_number > 1:
        image_prompt += f" Create a new scene that fits the story progression while maintaining visual consistency with previous illustrations."

    url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {stability_api_key}"
    }
    payload = {
        "text_prompts": [
            {"text": image_prompt, "weight": 1},
            {"text": "Create a child-friendly, colorful illustration", "weight": 0.5}
        ],
        "cfg_scale": 8,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 576,  # Changed from 512 to 576
        "width": 1024,  # Changed from 512 to 1024
        "samples": 1,
        "steps": 30,
        "style_preset": style,
        "seed": random.randint(0, 4294967295)
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        data = response.json()
        if "artifacts" in data and len(data["artifacts"]) > 0:
            image_data = base64.b64decode(data["artifacts"][0]["base64"])
            return BytesIO(image_data)
        else:
            print(f"No image data in response: {data}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error generating image: {str(e)}")
        return None

def generate_video(image_url, story_text, culture):
    url = "https://api.stability.ai/v2beta/image-to-video"
    headers = {
        "Authorization": f"Bearer {stability_api_key}",
        "Accept": "application/json"
    }
    
    prompt = f"Create a whimsical, child-friendly animation based on this bedtime story set in Timor-Leste for {culture['people']} children: {story_text}"
    
    local_image_path = download_image_from_s3(image_url)
    
    with open(local_image_path, "rb") as image_file:
        files = {
            "image": ("image.png", image_file, "image/png"),
        }
        data = {
            "seed": 0,
            "cfg_scale": 1.8,
            "motion_bucket_id": 127
        }
        
        response = requests.post(url, headers=headers, files=files, data=data)
        
    if response.status_code == 200:
        generation_id = response.json().get('id')
        return generation_id
    else:
        print(f"Error generating video: {response.text}")
        return None

def save_video_to_s3(video_content, video_name):
    bucket_name = 'tl-web'
    s3.put_object(
        Bucket=bucket_name,
        Key=f'videos/{video_name}',
        Body=video_content,
        ContentType='video/mp4'
    )
    return f"https://{bucket_name}.s3.us-west-2.amazonaws.com/videos/{video_name}"

def get_video_result(generation_id):
    url = f"https://api.stability.ai/v2beta/image-to-video/result/{generation_id}"
    headers = {
        "Authorization": f"Bearer {stability_api_key}",
        "Accept": "video/*"
    }
    
    max_attempts = 30
    for attempt in range(max_attempts):
        response = requests.get(url, headers=headers)
        if response.status_code == 202:
            print(f"Generation in progress, attempt {attempt + 1}/{max_attempts}")
            time.sleep(10)
        elif response.status_code == 200:
            return response.content
        else:
            print(f"Error retrieving video: {response.text}")
            return None
    
    print("Video generation timed out")
    return None
    
def download_image_from_s3(image_url):
    bucket_name = 'tl-web'
    key = image_url.split('tl-web/')[-1]  # Extract the key from the URL
    local_path = '/tmp/image.png'  # Use /tmp for Lambda's writable directory
    s3.download_file(bucket_name, key, local_path)
    return local_path
    
def lambda_handler(event, context):
    try:
        seed_file = load_random_file()
        story_content, selected_culture = generate_story(seed_file)  # Unpack both returned values
        
        # Parse the title
        title_parts = story_content[0].split('\n')
        english_title = title_parts[0].replace("Title (English): ", "").strip()
        tetun_title = title_parts[1].replace("Title (Tetun): ", "").strip()
        
        english_story_parts = []
        tetun_story_parts = []
        
        for part in story_content[1:]:
            part_lines = part.split('\n')
            if len(part_lines) >= 2:
                english_part = part_lines[0].split(': ', 1)[-1].strip()
                tetun_part = part_lines[1].split(': ', 1)[-1].strip()
                english_story_parts.append(english_part)
                tetun_story_parts.append(tetun_part)
        
        safe_title = ''.join(c if c.isalnum() else '_' for c in english_title.lower())
        date_str = datetime.now().strftime("%Y%m%d")
        
        # Choose a single style for the entire story
        styles = ['analog-film', 'anime', 'cinematic', 'comic-book', 'digital-art', 'enhance', 'fantasy-art', 'isometric', 'line-art', 'modeling-compound', 'neon-punk', 'origami', 'photographic', 'pixel-art', 'tile-texture']
        weights = [random.randint(1, 3) for _ in range(len(styles))]
        
        style = random.choices(styles, weights=weights)[0]
        print(f"Selected style: {style}")
        
        # Create a custom style description
        custom_style = f" Maintain a consistent art style across all illustrations. "

        image_urls = []
        for i, part in enumerate(english_story_parts, 1):
            image = generate_image(part[:300], style, selected_culture, custom_style, part_number=i)
            if image is not None:
                image_name = f'{safe_title}_image_{i}_{date_str}.png'
                image_url = save_image_to_s3(image, image_name)
                image_urls.append(image_url)
            else:
                print(f"Failed to generate image for part {i}")
        
        # Generate video
        #full_story_text = " ".join(english_story_parts)
        #f image_urls:
        #    video_generation_id = generate_video(image_urls[0], full_story_text, selected_culture)
        #else:
        #    print("No images were generated or there was an access issue, skipping video generation")
        #    video_generation_id = None
        
        #if video_generation_id:
        #    video_content = get_video_result(video_generation_id)
        #    if video_content:
        #        video_name = f'{safe_title}_video_{date_str}.mp4'
        #        video_url = save_video_to_s3(video_content, video_name)
        #    else:
        #        print("Failed to retrieve video content")
        #        video_url = None
        #else:
        #    print("Failed to start video generation")
        #    video_url = None

        html_content = generate_html(english_title, english_story_parts, image_urls, tetun_title, tetun_story_parts)
        
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
            'body': json.dumps(f"Bedtime story '{english_title}' for {selected_culture['people']} culture with {len(english_story_parts)} parts generated and saved to s3://tl-web/bedtime.html. Previous story archived.")
        }
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"An error occurred: {str(e)}")
        }