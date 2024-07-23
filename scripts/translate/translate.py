import os
import re
import json
from pathlib import Path
from openai import OpenAI

# Set the script directory
SCRIPT_DIR = Path(__file__).parent
DICT_FILE = SCRIPT_DIR / 'dictionary.js'
PHRASES_FILE = SCRIPT_DIR / 'phrases.js'

# Load dictionary
with open(DICT_FILE, 'r', encoding='utf-8') as f:
    dict_content = f.read()
    # Extract the dictionary content
    dict_start = dict_content.index('{')
    dict_end = dict_content.rindex('}') + 1
    english_to_tetum = json.loads(dict_content[dict_start:dict_end])

# Load phrases
with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
    phrases_content = f.read()
    # Extract the JSON content
    json_start = phrases_content.index('{')
    json_end = phrases_content.rindex('}') + 1
    tetum_phrases = json.loads(phrases_content[json_start:json_end])

# Set up OpenAI client
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
if not client.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

def translate_words(text, dictionary):
    words = re.findall(r'\b\w+\b|[.,!?;]', text.lower())
    translated_words = [dictionary.get(word, word) for word in words]
    return ' '.join(translated_words)

def clean_up_translation(original_text, dictionary_translation, phrases):
    phrases_context = "\n".join([f"{key}: {value}" for key, value in phrases.items()])
    
    prompt = f"""
Original English text: '{original_text}'
Initial dictionary-based translation to Tetum: '{dictionary_translation}'
Tetum phrases for context:
{phrases_context}

Please refine and complete this translation from English to Tetum. 
Use the dictionary translation as a starting point, but improve upon it 
where necessary for grammar, style, and accuracy. Translate any untranslated 
parts from the original text. Use the provided Tetum phrases as context to improve the translation.
Tetum is related to Portuguese, so use Portuguese for any idioms or words you don't know.
Provide only the final Tetum translation without any additional text or labels.
"""
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert translator between English and Tetum. Always attempt to complete and refine the translation, even if you're unsure about some parts. If you're not certain about specific terms, provide your best guess and indicate any uncertainties. Use the provided Tetum phrases as context to improve your translation. Provide only the final Tetum translation without any additional text or labels."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        temperature=0.7,
    )
    translation = response.choices[0].message.content.strip()
    
    # Remove any potential "Tetum Translation:" or similar prefixes
    translation = re.sub(r'^(Tetum Translation:?\s*)', '', translation, flags=re.IGNORECASE)
    
    return translation.strip()

def translate_file(file_path, max_words):
    file_path = Path(file_path)
    new_file_path = file_path.with_suffix('.tetum' + file_path.suffix)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check word count
    word_count = len(content.split())
    if word_count > max_words:
        print(f"Skipping {file_path}: Exceeds {max_words} word limit ({word_count} words)")
        return

    initial_translation = translate_words(content, english_to_tetum)
    final_translation = clean_up_translation(content, initial_translation, tetum_phrases)
    
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(final_translation)
    
    print(f"Translated {file_path} to {new_file_path}")

def get_files_to_translate(directory):
    files_to_translate = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            # Skip files that already have .tetum. in their name
            if '.tetum.' in file_path.name:
                continue
            if file_path.suffix.lower() in ['.txt', '.md', '.html']:
                tetum_file = file_path.with_suffix('.tetum' + file_path.suffix)
                if not tetum_file.exists():
                    files_to_translate.append(file_path)
    return files_to_translate

def translate_directory(directory, max_words):
    directory = Path(directory)
    if not directory.is_dir():
        print(f"Error: {directory} is not a valid directory")
        return

    files_to_translate = get_files_to_translate(directory)
    
    if not files_to_translate:
        print("No files found that need translation.")
        return

    print(f"Found {len(files_to_translate)} files to translate.")
    
    for file_path in files_to_translate:
        translate_file(file_path, max_words)

# Main execution
if __name__ == "__main__":
    directory_path = input("Enter the directory path to translate: ")
    
    while True:
        try:
            max_words = int(input("Enter the maximum number of words per file to translate (e.g., 1400): "))
            if max_words > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    translate_directory(directory_path, max_words)