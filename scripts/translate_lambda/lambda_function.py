import json
import os
import base64
from pathlib import Path
from anthropic import Anthropic
import tiktoken

print("Lambda function initialized")

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

# Set up Anthropic client
anthropic_client = Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

# Function to count tokens in a string
def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# Main function to translate English to Tetun
def translate_english_to_tetun(text):
    print("Translating text with Anthropic model")
    
    # Load dictionary contents
    with open(DICT_FILE, 'r', encoding='utf-8') as f:
        dictionary_content = f.read()
    with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
        phrases_content = f.read()
    with open(COMPOUND_FILE, 'r', encoding='utf-8') as f:
        compound_content = f.read()

    prompt = f"""Human: Translate the following English text to Tetun. When translating, please consider the following Tetun grammar rules:
    
    1. Word order: In Tetun, the verb often comes at the end of the sentence. If a sentence has 3 or more words and doesn't start with a pronoun (Hau, O, Nia, Ita, Ami, Imi, Sira), move the first word to the end of the sentence.
    
    2. Aspect markers: Use the following Tetun words:
       - 'ona' for completed actions (e.g., "Hau han ona" = "I have eaten")
       - 'tiha' for perfective aspect (e.g., "Hau han tiha" = "I ate")
       - 'hela' for continuous actions (e.g., "Hau han hela" = "I am eating")
       - 'sei' for future actions (e.g., "Hau sei han" = "I will eat")
    
    3. Pronouns: Use the following Tetun pronouns:
       - "Ha'u" for "I"
       - Ó (informal of 'you' specially used for children)
       - 'Ita' for 'you' (formal) or 'we' (inclusive)
       - 'Nia' for 'he/she/it'
       - 'Ami' for 'we' (exclusive)
       - 'Imi' for 'you' (plural)
       - 'Sira' for 'they'
    
    4. Use the possessive marker 'nia' between the possessor and the possessed item (e.g., - Maria-nia uma = Maria's house. (use hyphens to connect more than one subject together))
    
    5. Use 'mak' for focus or emphasis (e.g., "Maria mak han" = "It was Maria who ate")
    
    6. Use 'katak' to introduce reported speech or thoughts (e.g., "Nia dehan katak..." = "He said that...")

    7. Do not use "posessor" for "teacher" unless it is a male teacher; while for female teacher you should write "profesora". "manorin" is a general term for both female and male teachers.    
    Use the provided dictionaries to assist with the translation:
    
    Dictionary: {dictionary_content}
    Phrases: {phrases_content}
    Compound words: {compound_content}
    
    Please provide a full translation but use the Dictionary to help you with words you don't know in Tetun.
    
    Text to translate:
    {text}

    Human: Translate the text as described above, returning only the Tetun translation without any additional text.

    Assistant: [Tetun translation]

    Human: Thank you for translating. Please return this output exactly as is, with no additional text.

    Assistant: [Tetun translation]
    Assistant:"""

    response = anthropic_client.completions.create(
        prompt=prompt,
        model="claude-v1",
        max_tokens_to_sample=1000,
        stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
    )
    
    translation = response.completion.strip()
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
            'body': json.dumps({'translation': translation}),
            'headers': response_headers
        }
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'An error occurred during translation'}),
            'headers': response_headers
        }