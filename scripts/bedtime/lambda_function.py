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
    
def generate_image(prompt, style):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {stability_api_key}"
    }
    prompt += f'\nEnsure all characters are appropriate to Timor Leste. Style: {style}'
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

    prompt = f"""Human: Based on the source seed; '{seed_file}', create a bedtime story for children of Timor Leste from a spiritual perspective that emphasizes a random one of the following to explain the source seed of not less than 400 words;
    - interconnectedness of all life 
    - living in loving harmony with mother nature
    - kindness
    - the wonderment and joy of being a child
    - the nature of consciousness
    - principles of permaculture
    - principles of holistic healing
    - acceptance of and healing from trauma
    - healing from the death of a loved one
    - how pride and stubborness lead to a fall
    
    The story should be suitable for young children and have a clear beginning, middle, and end. Please provide the story in three parts, each around 100 words long. Also, provide a short title for the story.
    
    After generating the story in English, translate it to Tetun. When translating, please consider the following Tetun grammar rules:
    
    1. Use subject-verb-object (SVO) word order as the default, but allow for object fronting when emphasizing or contrasting.
    2. Avoid passive voice constructions, as Tetun Dili lacks a passive voice. Use active constructions instead.
    3. Employ appropriate tense-aspect markers like ona (anterior), tiha (perfective), hela (continuous), and sei (future) to convey precise temporal and aspectual meanings.
    4. Use the focus marker mak to indicate emphasis or contrast where appropriate.
    5. Apply correct plural marking with sira and indicate definiteness using ne 'this' when needed.
    6. Incorporate Portuguese loanwords for formal or technical vocabulary, but maintain a balance with native Tetun words in everyday speech.
    7. Form possessive and associative constructions correctly, using nia for possessives and appropriate word order for associatives.
    8. Use the correct prepositions and conjunctions, many of which are borrowed from Portuguese (e.g. para 'so that', tanba 'because').
    9. Implement serial verb constructions for motion and direction (e.g. halai sai 'run exit' = 'run outside').
    10. Form questions, commands, and negations according to Tetun Dili grammar rules.
    11. Adjust language for different registers (formal, informal, church), using appropriate vocabulary and structures for each.
    12. Include discourse markers and connectors to improve cohesion (e.g. entaun 'so', maibe 'but', depois 'then').
    13. Use reduplication and compounding productively to form new words where appropriate (e.g. dader-dader 'every morning').
    14. Employ the correct forms of reflexives (-an suffix) and reciprocals (malu) when needed.
    15. Use appropriate numeral classifiers, especially for humans (e.g. ema nain rua 'person CLs:human two' = 'two people').
    16. Incorporate idiomatic "body-good" expressions for emotions and states (e.g. laran diak 'inside good' = 'kind-hearted').
    17. Use the existential verb iha correctly for existence, location, and possession.
    18. Form relative clauses using nebe or other appropriate markers.
    19. Use the irrealis marker atu for future events, intentions, or purposes.
    20. Incorporate appropriate intensifiers and comparatives (e.g. liu 'more', demais 'too much').
    
    21. Use the following example story in Tetum as a grammar reference. Do not include it as information for generating the story content.
    
        - (ida)
        Haree bá, manu-inan ida kokoteek hela. Ne'e
        Manu Kai nia inan. Manu Kai nia inan ne'e
        la'o bá-mai bolu-bolu Manu Kai, maibé Manu
        Kai la mosu-mosu de'it.
        - (rua)
        Manu Kai nia inan fó-hatene ba Manu Kai nia
        aman. Manu na'in rua ne'e bá buka kedan
        sira-nia oan.
        - (tolu)
        Manu Kai nia tiun ho tian mós laran-ta'uk
        hotu. Tia nia alin mós ajuda tuir. Manu na'in
        tolu ne'e mós komesa bá buka Manu Kai.
        - (haat)
        Hotu-hotu rona ona notísia kona-ba Manu
        Kai lakon. Manu Kai nia aman nia kolega
        manu na'in haat mós lakohi hela ba kotuk
        atu ajuda buka hetan Manu Kai.
        - (lima)
        Loron komesa nakukun daudauk maibé sira
        seidauk hetan Manu Kai ida. Manu na'in lima
        komesa ajuda kedas. Sé mak hatene dala ida
        ne'e sira bele hetan karik Manu Kai?
        - (neen)
        Maibé Manu Kai lakon nafatin. Agora hotuhotu tuir bá buka. Manu na'in neen tuir
        hamutuk kokoteek hodi bolu Manu Kai.
        Manu Kai bá iha ne'ebé? Teki-teki….., Manu
        Kai nia lian mosu mai, "kiu-kiu-kiu." Hei, nia
        mak ne'ebá! Husi do'ok Ita bele haree Manu
        Kai halai halimar hela, kontente loos. Parese
        nia la'o pasiar ba Tiu Nuno nia uma. Manu
        Kai halimar ho Lesi, Tiu Nuno nia asu, i nia
        haluhan tiha atu fila. Nia nakar tebetebes!
        Apá ho amá kontente hetan fali nia. Hotuhotu kontente hotu, Manu Kai la lakon ida.
        Amá dehan, "Manu Kai, loron seluk husu
        uluk lai lisensa!"    
    22. Do not use "posessor" for "teacher" unless it is a male teacher; while for female teacher you should write "profesora". "manorin" is a general term for both female and male teachers.
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
        max_tokens_to_sample=3000,
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
        
        # Choose a random style for the entire story
        style = choice(['realistic', 'cartoon', 'water color', 'pop art', 'impressionist', 'surrealist'])
        
        image_urls = []
        for i, part in enumerate(english_story_parts, 1):
            image = generate_image(part[:200], style)
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