# English to Tetun Translation Script

This Python script allows you to translate English text files to Tetun using OpenAI's GPT-4 or Anthropic's Claude-3 language models. It provides a command-line interface for specifying the directory containing the files to translate, the maximum number of tokens per translation request, the AI model to use, and whether to allow processing of large files.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- Required Python packages: `openai`, `anthropic`, `nltk`, `stanza`, `tiktoken`
- OpenAI API key (set as an environment variable `OPENAI_API_KEY`)
- Anthropic API key (set as an environment variable `ANTHROPIC_API_KEY`)

## Setup

1. Clone the repository or download the `translate.py` script.

2. Install the required Python packages:
   ```
   pip install openai anthropic nltk stanza tiktoken
   ```

3. Set your OpenAI and Anthropic API keys as environment variables:
   ```
   export OPENAI_API_KEY=your_openai_api_key
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   ```

## Usage

To translate files, run the `translate.py` script with the following command:

```
python translate.py
```

The script will prompt you for the following information:

1. **Directory path**: Enter the path to the directory containing the files you want to translate.

2. **AI model**: Choose the AI model to use for translation (`openai` for GPT-4 or `anthropic` for Claude-3).

3. **Allow large file processing**: Specify whether to allow processing of large files (`yes` or `no`). If enabled, files exceeding the token limit will be split into chunks and translated separately.

The script will then scan the specified directory for files with `.txt`, `.md`, or `.html` extensions and translate them one by one.

## Translation Process

The translation process for each file consists of the following steps:

1. **Preprocessing**: The English text is preprocessed by applying Tetun word order rules, translating aspect markers and pronouns, handling compound words, and handling reduplication.

2. **Initial translation**: The preprocessed text is translated word by word using a dictionary loaded from the `dictionary.js` file.

3. **Co-occurrence-based improvement**: The initial translation is improved by considering the co-occurrence of English and Tetun words in phrases loaded from the `phrases.js` file. The most likely Tetun words are selected based on their co-occurrence frequency.

4. **AI model translation**: The improved translation is sent to the selected AI model (GPT-4 or Claude-3) for final translation, taking into account Tetun grammar rules.

5. **Saving the translation**: The translated text is saved to a new file with the same name as the original file, appended with `.tetum` before the file extension.

Here's an example of how a file is translated:

```python
def translate_file(file_path, max_tokens, model, allow_large_files):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Preprocess the text
    preprocessed_text = preprocess_text(content)

    # Perform initial word-level translation
    initial_translation = translate_words(preprocessed_text, english_to_tetun)

    # Improve translation using co-occurrence
    improved_translation = improve_translation(initial_translation)

    # Translate using the selected AI model
    translation = translate_english_to_tetun(improved_translation, model)

    # Save the translation to a new file
    new_file_path = file_path.with_suffix('.tetum' + file_path.suffix)
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(translation)
```

## Large File Handling

If the `allow_large_files` option is enabled, files that exceed the token limit will be split into chunks and translated separately. The translated chunks are then combined to form the final translation.

Here's an example of how a large file is translated:

```python
def translate_large_file(file_path, max_tokens, model):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into chunks
    chunks = split_into_chunks(content, max_tokens)

    # Translate each chunk separately
    translated_chunks = []
    for chunk in chunks:
        translation = translate_english_to_tetun(chunk, model)
        translated_chunks.append(translation)

    # Combine the translated chunks
    full_translation = '\n\n'.join(translated_chunks)

    # Save the full translation to a new file
    new_file_path = file_path.with_suffix('.tetum' + file_path.suffix)
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(full_translation)
```

## Conclusion

The English to Tetun translation script provides an automated way to translate text files using state-of-the-art language models. By leveraging preprocessing techniques, dictionary-based translation, co-occurrence-based improvement, and AI model translation, the script aims to produce accurate and fluent translations from English to Tetun.

Feel free to explore the script and adapt it to your specific needs. If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository.