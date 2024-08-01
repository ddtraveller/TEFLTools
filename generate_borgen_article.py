import anthropic
import os
import re
import requests
from bs4 import BeautifulSoup
import time
import json
import PyPDF2
import tiktoken
import shutil
import zipfile
import xml.etree.ElementTree as ET

# Initialize the Anthropic client
# export ANTHROPIC_API_KEY='your_api_key_here'
client = anthropic.Anthropic()

def clean_name(name):
    """Clean the name to be safe for file systems and folder names."""
    cleaned = re.sub(r'[^\w\-_\. ]', '', name)
    cleaned = re.sub(r'\s+', '_', cleaned)
    return cleaned.lower()

def create_directory(path):
    """Create a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    print(f"Created directory: {path}")

def read_docx(path):
    """Read text from a .docx file."""
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = ET.XML(xml_content)
    
    paragraphs = []
    for paragraph in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        texts = [node.text for node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
        if texts:
            paragraphs.append(''.join(texts))
    
    return '\n\n'.join(paragraphs)

def read_file_content(file_path):
    """Read content from PDF, TXT, MD, or DOCX files."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == '.pdf':
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            return "\n".join([page.extract_text() for page in pdf_reader.pages])
    elif ext in ['.txt', '.md']:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif ext == '.docx':
        try:
            return read_docx(file_path)
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            return ""
    else:
        print(f"Unsupported file format: {file_path}")
        return ""

def write_to_file(content, file_path):
    """Write content to a file and print confirmation."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Written file: {file_path}")

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def truncate_to_token_limit(text: str, max_tokens: int = 199999) -> str:
    """Truncates the text to fit within the specified token limit."""
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    if len(tokens) <= max_tokens:
        return text
    return encoding.decode(tokens[:max_tokens])

def generate_article(truncated_info, article_topic):
    """Generate an AP article about"""
    prompt = f"""Given the following information:
    {truncated_info}
    Write an article about {article_topic}.
    Articles should be written in AP Style.
    Word count. 400-500 words
    Three or more sources. Use at least three distinct sources (borgenproject.org and borgenmagazine.com cannot be used as sources). List hyperlinks for your sources alphabetically at the bottom of your article.
    Write in the “Inverted Pyramid.” Begin your article with a gripping lede under 35 words. Include the most important information at the top, and trickle down to your supplementary and supporting information.
    Avoid clunky paragraphs. This isn’t a college essay. Paragraphs should be short enough to keep readers moving to the next one, but long enough to give readers the information they need. Aim for 2-3 sentences. Be specific in your information, attributing your information when possible; don’t over-generalize.
    Concise content. Write in short, grammatically correct sentences. Do not use the passive voice. Use active verbs, good adjectives and not too many superlatives.
    Readers have a very brief attention span. Grab their attention with figures and information; provide fascinating facts. Use a list format or subheadings where appropriate.
    Titles should be short and very clear. Anybody reading your title should know what you’re trying to say.
    Report and write in the third person. You are reporting information and stating fact, not belief. Do not use “I,” “you” or “we.”
    Avoid long quotes and multiple quotes per paragraph. Be sure to properly attribute your quotes. Don’t rely too heavily on quotes; paraphrase when applicable.
    There is a time and a place for stylistic flare. We love to see the punchy, one-sentence-long paragraphs, the rhetorical questions, the em-dashes and other bits of stylistic flair, but only when it’s done sparingly. Do not rely on it as a crutch.
    Don't add any text or commentary before or after the article"""
        
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4000,
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    time.sleep(2)  # Pause for 2 seconds after Anthropic call
    return message.content[0].text if message.content else ""

def fetch_and_clean_url_content(url):
    """Fetch content from URL and clean it using Anthropic."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        text_content = soup.get_text()
        
        prompt = f"Clean and format the following text content from a webpage, removing any irrelevant information and preserving only the main text content:\n\n{text_content[:2000]}..."

        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2000,
            temperature=0,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        time.sleep(2)  # Pause for 2 seconds after Anthropic call
        return message.content[0].text if message.content else ""
    except Exception as e:
        print(f"Error fetching or cleaning URL content: {str(e)}")
        return ""

def analyze_all_content(content_folder):
    """Analyze all PDF content and determine an inclusive course topic."""
    all_content = ""
    for filename in os.listdir(content_folder):
        if filename.lower().endswith('.pdf'):
            print(f"Reading: {filename}")
            file_path = os.path.join(content_folder, filename)
            all_content += read_file_content(file_path) + "\n\n"
            print(f"Read content from: {file_path}")

    prompt = f"""Analyze the following content from multiple PDF files and provide a summary of the main topics and themes. This will be used to generate a course syllabus, so focus on identifying overarching themes and key areas of study:

{all_content[:50000]}  # Limit to first 50000 characters to fit within token limits

Based on this content, suggest an inclusive course topic that encompasses the major themes found in all the documents. Your response should be structured as follows:

1. Main Course Topic: [Suggested course topic]
2. Key Themes:
   - [Theme 1]
   - [Theme 2]
   - [Theme 3]
   ...
3. Brief Overview: [2-3 sentences summarizing the content and its relevance to the course topic]
"""

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    time.sleep(2)  # Pause for 2 seconds after Anthropic call
    return message.content[0].text if message.content else ""

def main():
    article_topic = input("Enter the article topic: ")

    content_folder = 'content'
    
    topic = analyze_all_content(content_folder)
    print("Topic analysis complete.")
    
    project_info = ""
    for filename in os.listdir(content_folder):
        if filename.lower().endswith(('.pdf', '.txt', '.md', '.docx')):
            file_path = os.path.join(content_folder, filename)
            project_info += read_file_content(file_path) + "\n\n"
        
    print(f"Total content size before truncation: {len(project_info)} characters")
    truncated_info = truncate_to_token_limit(project_info, max_tokens=170000)
    print(f"Truncated content size: {len(truncated_info)} characters")
    
    article = generate_article(truncated_info, article_topic) 
    write_to_file(article, './generated_article.txt')

if __name__ == "__main__":
    main()