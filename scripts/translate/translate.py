import os
import re
import json
from pathlib import Path
from openai import OpenAI

# Set the script directory
SCRIPT_DIR = Path(__file__).parent
DICT_FILE = SCRIPT_DIR / 'dictionary.js'

# Load dictionary
with open(DICT_FILE, 'r') as f:
    dict_content = f.read()
    # Extract the dictionary content
    dict_start = dict_content.index('{')
    dict_end = dict_content.rindex('}') + 1
    english_to_tetum = json.loads(dict_content[dict_start:dict_end])

# Set up OpenAI client
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
if not client.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

def translate_words(text, dictionary):
    words = re.findall(r'\b\w+\b|[.,!?;]', text.lower())
    translated_words = [dictionary.get(word, word) for word in words]
    return ' '.join(translated_words)

def clean_up_translation(original_text, dictionary_translation):
    prompt = f"""
Original English text: '{original_text}'
Initial dictionary-based translation to Tetum: '{dictionary_translation}'
Please refine and complete this translation from English to Tetum. 
Use the dictionary translation as a starting point, but improve upon it 
where necessary for grammar, style, and accuracy. Translate any untranslated 
parts from the original text. Tetum is related to Portuguese so use Portuguese for any idioms or words you don't know.
Provide only the final Tetum translation without any additional text or labels.
"""
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert translator between English and Tetum. Always attempt to complete and refine the translation, even if you're unsure about some parts. If you're not certain about specific terms, provide your best guess and indicate any uncertainties. Provide only the final Tetum translation without any additional text or labels."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,
        temperature=0.7,
    )
    translation = response.choices[0].message.content.strip()
    
    # Remove any potential "Tetum Translation:" or similar prefixes
    translation = re.sub(r'^(Tetum Translation:?\s*)', '', translation, flags=re.IGNORECASE)
    
    return translation.strip()

def translate_file(file_path, overwrite_all=False, skip_all=False):
    file_path = Path(file_path)
    if not file_path.is_file():
        print(f"Skipping {file_path}: Not a file")
        return overwrite_all, skip_all

    # Skip files with '.tetum.' in the name
    if '.tetum.' in file_path.name:
        print(f"Skipping {file_path}: Already a translation file")
        return overwrite_all, skip_all

    new_file_path = file_path.with_suffix('.tetum' + file_path.suffix)
    
    if new_file_path.exists() and not overwrite_all and not skip_all:
        while True:
            choice = input(f"Translation file {new_file_path} already exists. Overwrite? (y/n/a/s): ")
            if choice.lower() == 'y':
                break
            elif choice.lower() == 'n':
                print(f"Skipping {file_path}")
                return overwrite_all, skip_all
            elif choice.lower() == 'a':
                overwrite_all = True
                break
            elif choice.lower() == 's':
                skip_all = True
                print(f"Skipping {file_path}")
                return overwrite_all, skip_all
            else:
                print("Invalid choice. Please enter 'y' for yes, 'n' for no, 'a' for overwrite all, or 's' for skip all.")
    
    if new_file_path.exists() and skip_all:
        print(f"Skipping {file_path}")
        return overwrite_all, skip_all

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check word count
    word_count = len(content.split())
    if word_count > 1400:
        print(f"Skipping {file_path}: Exceeds 1400 word limit ({word_count} words)")
        return overwrite_all, skip_all

    initial_translation = translate_words(content, english_to_tetum)
    final_translation = clean_up_translation(content, initial_translation)
    
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(final_translation)
    
    print(f"Translated {file_path} to {new_file_path}")
    
    return overwrite_all, skip_all

def translate_directory(directory):
    directory = Path(directory)
    if not directory.is_dir():
        print(f"Error: {directory} is not a valid directory")
        return

    overwrite_all = False
    skip_all = False

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in ['.txt', '.md', '.html'] and '.tetum.' not in file_path.name:
                overwrite_all, skip_all = translate_file(file_path, overwrite_all, skip_all)

# Main execution
if __name__ == "__main__":
    directory_path = input("Enter the directory path to translate: ")
    translate_directory(directory_path)