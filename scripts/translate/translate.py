import os
import re
import json
import tiktoken
import math
from pathlib import Path
from openai import OpenAI
import anthropic

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
openai_client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
if not openai_client.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Set up Anthropic client
anthropic_client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
if not anthropic_client.api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def translate_words(text, dictionary):
    words = re.findall(r'\b\w+\b|[.,!?;]', text.lower())
    translated_words = [dictionary.get(word, word) for word in words]
    return ' '.join(translated_words)

def clean_up_translation(original_text, dictionary_translation, phrases, model):
    max_phrases = 5
    phrases_context = "\n".join([f"{key}: {value}" for key, value in list(phrases.items())[:max_phrases]])
    
    prompt = f"""Translate to Tetum:
'{original_text}'
Initial: '{dictionary_translation}'
Context:
{phrases_context}
Improve grammar and style. Use Portuguese for unknown words."""

    if model == "openai":
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert Tetum translator. Provide only the final translation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.7,
        )
        translation = response.choices[0].message.content.strip()
    elif model == "anthropic":
        response = anthropic_client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1024,
            temperature=0.7,
            system="You are an expert Tetum translator. Provide only the final translation.",
            messages=[{"role": "user", "content": prompt}]
        )
        translation = response.content[0].text.strip()
    
    return translation

def translate_large_file(file_path, max_tokens, model):
    file_path = Path(file_path)
    new_file_path = file_path.with_suffix('.tetum' + file_path.suffix)

    if new_file_path.exists():
        print(f"Skipping {file_path}: Destination file {new_file_path} already exists")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    total_tokens = num_tokens_from_string(content)
    num_chunks = math.ceil(total_tokens / max_tokens)
    
    if num_chunks > 10:
        print(f"Skipping {file_path}: File would be split into {num_chunks} chunks (more than 10)")
        return

    print(f"File will be split into {num_chunks} chunks.")
    
    chunk_size = math.ceil(len(content) / num_chunks)
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
    
    translated_chunks = []
    for i, chunk in enumerate(chunks, 1):
        print(f"Translating chunk {i} of {num_chunks}...")
        initial_translation = translate_words(chunk, english_to_tetum)
        final_translation = clean_up_translation(chunk, initial_translation, tetum_phrases, model)
        translated_chunks.append(final_translation)
    
    full_translation = '\n\n'.join(translated_chunks)
    
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(full_translation)
    
    print(f"Translated {file_path} to {new_file_path} in {num_chunks} chunks")

def translate_file(file_path, max_tokens, model, allow_large_files):
    file_path = Path(file_path)
    new_file_path = file_path.with_suffix('.tetum' + file_path.suffix)

    if new_file_path.exists():
        print(f"Skipping {file_path}: Destination file {new_file_path} already exists")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    total_tokens = num_tokens_from_string(content)
    effective_max_tokens = max_tokens - 200  # Reserve some tokens for prompt and overhead
    
    if total_tokens > effective_max_tokens:
        if allow_large_files:
            print(f"File {file_path} exceeds {effective_max_tokens} token limit ({total_tokens} tokens). Using chunk translation.")
            translate_large_file(file_path, effective_max_tokens, model)
        else:
            print(f"Skipping {file_path}: File exceeds token limit ({total_tokens} tokens) and large file processing is disabled.")
        return

    initial_translation = translate_words(content, english_to_tetum)
    final_translation = clean_up_translation(content, initial_translation, tetum_phrases, model)
    
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

def translate_directory(directory, max_tokens, model, allow_large_files):
    directory = Path(directory)
    if not directory.is_dir():
        print(f"Error: {directory} is not a valid directory")
        return
    
    #files_to_translate = sorted(get_files_to_translate(directory), reverse=True)
    files_to_translate = sorted(get_files_to_translate(directory))
    
    if not files_to_translate:
        print("No files found that need translation.")
        return

    print(f"Found {len(files_to_translate)} files to translate.")
    
    for file_path in files_to_translate:
        translate_file(file_path, max_tokens, model, allow_large_files)

# Main execution
if __name__ == "__main__":
    directory_path = input("Enter the directory path to translate: ")
    
    max_tokens = 2000  # Adjusted to 2000

    while True:
        model = input("Choose the model to use (openai/anthropic): ").lower()
        if model in ["openai", "anthropic"]:
            break
        print("Invalid choice. Please enter 'openai' or 'anthropic'.")

    while True:
        allow_large_files_input = input("Allow processing of large files? (yes/no): ").lower()
        if allow_large_files_input in ["yes", "no"]:
            allow_large_files = allow_large_files_input == "yes"
            break
        print("Invalid choice. Please enter 'yes' or 'no'.")

    translate_directory(directory_path, max_tokens, model, allow_large_files)