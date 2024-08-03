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

def translate_english_to_tetun(text):
    print("Translating text with Anthropic model")
    
    # Load dictionary contents
    with open(DICT_FILE, 'r', encoding='utf-8') as f:
        dictionary_content = f.read()
    with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
        phrases_content = f.read()
    with open(COMPOUND_FILE, 'r', encoding='utf-8') as f:
        compound_content = f.read()
    
    # Adaptive token usage
    input_tokens = num_tokens_from_string(text)
    max_tokens = min(4000, input_tokens * 2)  # Adjust as needed
    
    prompt = f"""Human: Translate the following English text to Tetun. When translating, please consider the following Tetun grammar rules:
    
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
        max_tokens_to_sample=max_tokens,
        stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
    )
    
    initial_translation = response.completion.strip()
    
    # Post-processing and context preservation check
    review_prompt = f"""Human: Please review the following English text and its Tetun translation. Ensure that the translation is grammatically correct, preserves the context of the original text, and follows Tetun grammar rules. If there are any issues, please provide a corrected version of the translation.

    English text:
    {text}

    Tetun translation:
    {initial_translation}

    Human: Please provide your review and, if necessary, a corrected version of the translation.

    Assistant: [Review and corrected translation if needed]

    Human: Thank you for the review. If you provided a corrected translation, please return only that translation. If no corrections were needed, please return the original translation exactly as is, with no additional text.

    Assistant: [Final translation]
    Assistant:"""
    
    review_response = anthropic_client.completions.create(
        prompt=review_prompt,
        model="claude-v1",
        max_tokens_to_sample=max_tokens,
        stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
    )
    
    final_translation = review_response.completion.strip()
    return final_translation

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