import os
import re
import json
import tiktoken
import math
from pathlib import Path
from openai import OpenAI
import anthropic
from nltk.corpus import stopwords
from nltk.probability import FreqDist, ConditionalFreqDist
import stanza
from gtts import gTTS
from pydub import AudioSegment

print("Script started")

# Set the script directory and file paths
SCRIPT_DIR = Path(__file__).parent
DICT_FILE = SCRIPT_DIR / 'dictionary.js' 
PHRASES_FILE = SCRIPT_DIR / 'phrases.js'
COMPOUND_FILE = SCRIPT_DIR / 'compound.js'

print(f"Script directory: {SCRIPT_DIR}")
print(f"Dictionary file: {DICT_FILE}") 
print(f"Phrases file: {PHRASES_FILE}")
print(f"Compound file: {COMPOUND_FILE}")

# Load dictionary from file
with open(DICT_FILE, 'r', encoding='utf-8') as f:
    dict_content = f.read()
    dict_start = dict_content.index('{')
    dict_end = dict_content.rindex('}') + 1
    english_to_tetun = json.loads(dict_content[dict_start:dict_end])

print(f"Loaded {len(english_to_tetun)} entries from dictionary")

# Load phrases from file  
with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
    phrases_content = f.read()
    json_start = phrases_content.index('{')
    json_end = phrases_content.rindex('}') + 1
    tetun_phrases = json.loads(phrases_content[json_start:json_end])

print(f"Loaded {len(tetun_phrases)} phrases")

# Load compounds from file
with open(COMPOUND_FILE, 'r', encoding='utf-8') as f:  
    compounds_content = f.read()
    json_start = compounds_content.index('{')
    json_end = compounds_content.rindex('}') + 1
    tetun_compounds = json.loads(compounds_content[json_start:json_end])

print(f"Loaded {len(tetun_compounds)} compounds")

# Set up OpenAI client
openai_client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
if not openai_client.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

print("OpenAI client set up")

# Set up Anthropic client
anthropic_client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
if not anthropic_client.api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

print("Anthropic client set up")

# Set up Stanza NLP pipeline for English
stanza.download('en', verbose=False)
en_nlp = stanza.Pipeline('en', processors='tokenize,pos')
print("Stanza English NLP pipeline set up")

# Function to count tokens in a string
def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# Function to translate words using the dictionary
def translate_words(text, dictionary):
    doc = en_nlp(text)
    translated_text = []
    for sent in doc.sentences:
        for word in sent.words:
            if word.lemma is not None:
                lemma = word.lemma.lower()
            else:
                lemma = word.text.lower()
            translated = dictionary.get(lemma, word.text)
            # Handle multi-word tokens
            if word.text.lower() != lemma and lemma in dictionary:
                translated = dictionary.get(lemma, word.text)
            translated_text.append(translated)
    return ' '.join(translated_text)

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

# Function to rank the most likely Tetun words for an English word using co-occurrence 
def get_best_tetun_words(english_word, cfd, n=5):
    if english_word in cfd.conditions(): 
        return cfd[english_word].most_common(n)
    else:
        return []

# Function to generate audio from text
def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='pt', slow=False)
    tts.save(output_file)
    print(f"Audio file saved: {output_file}")

# Main function to translate English to Tetun
def translate_english_to_tetun(text, model):
    print(f"Translating text with {model} model:")  
    print(f"Original text: {text[:100]}...")  # Print first 100 characters

    # Preprocess the text 
    preprocessed_text = preprocess_text(text)

    print(f"Preprocessed text: {preprocessed_text[:100]}...")  # Print first 100 characters

    # Perform initial word-level translation
    initial_translation = translate_words(preprocessed_text, english_to_tetun)

    print(f"Initial translation: {initial_translation[:100]}...")  # Print first 100 characters

    # Build co-occurrence matrix
    cfd = ConditionalFreqDist()
    for phrase, translation in tetun_phrases.items():
        english_words = phrase.lower().split()
        tetun_words = translation.lower().split()  
        for i in range(len(english_words)):
            for j in range(len(tetun_words)):
                cfd[english_words[i]][tetun_words[j]] += 1

    # Improve translation using co-occurrence 
    words = initial_translation.split()
    improved_words = []
    for word in words:
        if word in english_to_tetun:
            improved_words.append(english_to_tetun[word]) 
        else:
            best_tetun_words = get_best_tetun_words(word, cfd)
            if best_tetun_words:
                improved_words.append(best_tetun_words[0][0])
            else:
                improved_words.append(word)
    improved_translation = ' '.join(improved_words)

    print(f"Improved translation: {improved_translation[:100]}...")  # Print first 100 characters

    # Prepare the prompt for the AI model
    prompt = f"Translate the following English text to Tetun, keeping in mind Tetun grammar rules:\n\n{improved_translation}\n\nTetun translation:"

    # Use the specified AI model for translation
    if model == "openai":
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an English to Tetun translator."},
                {"role": "user", "content": prompt} 
            ],
            max_tokens=4096,
            temperature=0.7,
        )
        translation = response.choices[0].message.content.strip()
    elif model == "anthropic":
        response = anthropic_client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4096,
            temperature=0.7,
            system="You are an English to Tetun translator.",
            messages=[{"role": "user", "content": prompt}] 
        )
        translation = response.content[0].text.strip()

    print(f"Translation result: {translation[:100]}...")  # Print first 100 characters  
    return translation

# Function to translate large files by splitting them into chunks
def translate_large_file(file_path, max_tokens, model):
    print(f"Translating large file: {file_path}")  
    file_path = Path(file_path)  
    new_file_path = file_path.with_suffix('.tetum' + file_path.suffix)
    audio_file_path = file_path.with_suffix('.tetum.mp3')

    if new_file_path.exists() and audio_file_path.exists():
        print(f"Skipping {file_path}: Destination files already exist") 
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    total_tokens = num_tokens_from_string(content)
    num_chunks = math.ceil(total_tokens / max_tokens)  

    print(f"File has {total_tokens} tokens, will be split into {num_chunks} chunks")

    if num_chunks > 10:
        print(f"Skipping {file_path}: File would be split into {num_chunks} chunks (more than 10)") 
        return

    chunk_size = math.ceil(len(content) / num_chunks)
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]

    translated_chunks = []  
    audio_segments = []
    for i, chunk in enumerate(chunks, 1):
        print(f"Translating chunk {i} of {num_chunks}...")
        translation = translate_english_to_tetun(chunk, model)
        translated_chunks.append(translation)  

        # Generate audio for this chunk
        chunk_audio_file = f"temp_chunk_{i}.mp3"
        text_to_speech(translation, chunk_audio_file)
        audio_segments.append(AudioSegment.from_mp3(chunk_audio_file))

    full_translation = '\n\n'.join(translated_chunks)

    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(full_translation)

    # Combine audio segments
    combined_audio = sum(audio_segments)
    combined_audio.export(str(audio_file_path), format="mp3")

    # Clean up temporary audio files
    for i in range(1, num_chunks + 1):
        os.remove(f"temp_chunk_{i}.mp3")

    print(f"Translated {file_path} to {new_file_path} and {audio_file_path} in {num_chunks} chunks")

# Function to translate a single file 
def translate_file(file_path, max_tokens, model, allow_large_files):
    print(f"Translating file: {file_path}")
    file_path = Path(file_path)
    new_file_path = file_path.with_suffix('.tetum' + file_path.suffix)
    audio_file_path = file_path.with_suffix('.tetum.mp3')

    if new_file_path.exists() and audio_file_path.exists():
        print(f"Skipping {file_path}: Destination files already exist")
        return 

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    total_tokens = num_tokens_from_string(content)  
    effective_max_tokens = max_tokens - 200  # Reserve some tokens for prompt and overhead

    print(f"File has {total_tokens} tokens, effective max tokens: {effective_max_tokens}")  

    if total_tokens > effective_max_tokens:
        if allow_large_files:  
            print(f"File {file_path} exceeds {effective_max_tokens} token limit ({total_tokens} tokens). Using chunk translation.")
            translate_large_file(file_path, effective_max_tokens, model)
        else:
            print(f"Skipping {file_path}: File exceeds token limit ({total_tokens} tokens) and large file processing is disabled.")
        return

    translation = translate_english_to_tetun(content, model)

    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(translation)

    print(f"Translated {file_path} to {new_file_path}")

    # Generate audio file
    text_to_speech(translation, str(audio_file_path))

# Function to get all files that need translation in a directory 
def get_files_to_translate(directory):
    print(f"Scanning directory for files to translate: {directory}")  
    files_to_translate = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            if '.tetum.' in file_path.name:  
                continue
            if file_path.suffix.lower() in ['.txt', '.md', '.html']:  
                tetum_file = file_path.with_suffix('.tetum' + file_path.suffix)
                audio_file = file_path.with_suffix('.tetum.mp3')
                if not tetum_file.exists() or not audio_file.exists():
                    files_to_translate.append(file_path)
    print(f"Found {len(files_to_translate)} files to translate")
    return files_to_translate

# Function to translate all files in a directory
def translate_directory(directory, max_tokens, model, allow_large_files):
    print(f"Translating directory: {directory}")
    directory = Path(directory)
    if not directory.is_dir():
        print(f"Error: {directory} is not a valid directory")
        return

    files_to_translate = sorted(get_files_to_translate(directory))

    if not files_to_translate:
        print("No files found that need translation.")
        return

    print(f"Found {len(files_to_translate)} files to translate.")

    for file_path in files_to_translate:
        translate_file(file_path, max_tokens, model, allow_large_files)

# Main execution
if __name__ == "__main__":
    print("Starting main execution") 
    # Get user input for directory path
    directory_path = input("Enter the directory path to translate: ")

    max_tokens = 4000  # Set maximum tokens to 4000
    print(f"Maximum tokens set to: {max_tokens}") 

    # Get user input for AI model choice  
    while True:
        model = input("Choose the model to use (openai/anthropic): ").lower()
        if model in ["openai", "anthropic"]:
            break 
        print("Invalid choice. Please enter 'openai' or 'anthropic'.")

    # Get user input for allowing large file processing
    while True:
        allow_large_files_input = input("Allow processing of large files? (yes/no): ").lower()
        if allow_large_files_input in ["yes", "no"]:
            allow_large_files = allow_large_files_input == "yes"
            break
        print("Invalid choice. Please enter 'yes' or 'no'.")

    print(f"Starting translation process with model: {model}, allow large files: {allow_large_files}")
    # Start the translation process   
    translate_directory(directory_path, max_tokens, model, allow_large_files)
    print("Translation process completed")