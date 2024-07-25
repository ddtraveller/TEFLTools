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

# Function to translate words using the dictionary
def translate_words(text, dictionary):
    words = text.lower().split()
    return ' '.join(dictionary.get(word, word) for word in words)

# Placeholder for other helper functions
def preprocess_text(text):
    # Implement preprocessing logic here
    return text

# Main function to translate English to Tetun
def translate_english_to_tetun(text):
    print("Translating text with Anthropic model")
    
    # Preprocess and perform initial translation
    preprocessed_text = preprocess_text(text)
    initial_translation = translate_words(preprocessed_text, english_to_tetun)
    
    # Prepare the prompt for the AI model
    prompt = f"Translate the following English text to Tetun, keeping in mind Tetun grammar rules:\n\n{initial_translation}\n\nTetun translation:"

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
    
    # Check if the event contains the file content
    if 'body' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('No file content found in the request')
        }

    # Decode the base64-encoded file content
    file_content = base64.b64decode(event['body']).decode('utf-8')

    print("Translating file content")

    # Perform the translation
    translation = translate_english_to_tetun(file_content)

    # Return the translated content
    return {
        'statusCode': 200,
        'body': json.dumps({'translation': translation}),
        'headers': {
            'Content-Type': 'application/json'
        }
    }