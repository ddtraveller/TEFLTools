import json
import os
import base64
from pathlib import Path
import anthropic
import tiktoken

print("Lambda function initialized")

# Set up paths (in Lambda, we'll use /tmp for writable storage)
SCRIPT_DIR = Path('/tmp')
DICT_FILE = SCRIPT_DIR / 'dictionary.js'
PHRASES_FILE = SCRIPT_DIR / 'phrases.js'
COMPOUND_FILE = SCRIPT_DIR / 'compound.js'

# Load dictionary, phrases, and compounds
# Note: In a real Lambda, you'd need to ensure these files are available,
# possibly by including them in your deployment package or downloading them at runtime
# Assume these are loaded and available as dictionaries:
english_to_tetun = {}  # Load this from DICT_FILE
tetun_phrases = {}  # Load this from PHRASES_FILE
tetun_compounds = {}  # Load this from COMPOUND_FILE

# Set up Anthropic client
anthropic_client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

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
        text = text.replace(f" {marker} ", f" {translation} ")
    return text

# Dictionary of Tetun pronouns and their English equivalents
pronoun_map = {
    'Hau': 'I',
    'O': 'you (informal)', 
    'Ita': 'you (formal)/we (inclusive)',
    'Nia': 'he/she/it',
    'Ami': 'we (exclusive)',
    'Imi' : 'you (plural)',
    'Sira': 'they'
}

# Function to translate Tetun pronouns
def translate_pronouns(text):
    for tetun, english in pronoun_map.items():
        text = text.replace(f" {tetun} ", f" {english} ")
    return text

# Function to translate Tetun compound words
def translate_compounds(text):
    for compound, translation in tetun_compounds.items():
        text = text.replace(compound, translation)
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
    prompt = f"Translate the following English text to Tetun, keeping in mind Tetun grammar rules:\n\n{preprocessed_text}\n\nTetun translation:"
    response = anthropic_client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        temperature=0.7,
        system="You are an English to Tetun translator.",
        messages=[{"role": "user", "content": prompt}]
    )
    translation = response.content[0].text.strip()
    return translation

def lambda_handler(event, context):
    print("Lambda handler invoked")
    print(f"Received event: {json.dumps(event)}")  # Log the entire event for debugging
    
    response_headers = {
        'Access-Control-Allow-Origin': 'https://go-tl.com',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST,OPTIONS',
        'Content-Type': 'application/json'
    }
    
    # Check if this is an OPTIONS request
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': response_headers
        }
    
    # Check for the presence of the body in different possible locations
    body = event.get('body') or event.get('content') or event.get('input')
    
    if not body:
        return {
            'statusCode': 400,
            'body': json.dumps('No file content found in the request'),
            'headers': response_headers
        }
    
    try:
        # Check if the body is base64 encoded
        if event.get('isBase64Encoded', False):
            file_content = base64.b64decode(body).decode('utf-8')
        else:
            file_content = body
        
        # If file_content is a string representation of a JSON object, parse it
        if isinstance(file_content, str):
            try:
                file_content = json.loads(file_content)
            except json.JSONDecodeError:
                pass  # It's not JSON, treat it as plain text
        
        # If file_content is a dict, extract the 'content' field
        if isinstance(file_content, dict):
            file_content = file_content.get('content', '')
        
        print("Translating file content")
        translation = translate_english_to_tetun(file_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'translation': translation})
        }
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'An error occurred during translation'}),
            'headers': response_headers
        }