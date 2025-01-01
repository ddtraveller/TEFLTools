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
    prompt = f"""
    Write an AP-style news article.
    Use the following information to support the thesis of the story:
    {truncated_info}
    Use the following rules to generate the AP-style news article.
    
    Guidelines:
    1. Article length: 400-500 words
    
    2. Sources: Use at least three distinct, credible sources. Exclude borgenproject.org and borgenmagazine.com. List source URLs alphabetically at the end of the article.
    
    3. Structure: Follow the "Inverted Pyramid" format:
       - Begin with a compelling lede under 35 words
       - Present the most crucial information first
       - Follow with supporting details in descending order of importance
    
    4. Paragraphs: Keep them concise (2-3 sentences) to maintain reader engagement. Provide specific, attributed information.
    
    5. Writing style:
       - Use short, grammatically correct sentences
       - Employ active voice and strong verbs
       - Avoid passive voice and excessive superlatives
       - Write in third person (no "I," "you," or "we")
       - Use AP style for punctuation, capitalization, and formatting
    
    6. Content:
       - Grab attention with relevant facts and figures
       - Use subheadings or lists where appropriate to break up text
       - Avoid long or multiple quotes in a single paragraph
       - Attribute quotes properly and paraphrase when suitable
    
    7. Title: Create a clear, concise headline that accurately reflects the article's content
    
    8. Dates and times: Follow AP style guidelines (e.g., spell out months when used alone, abbreviate when used with a date)
    
    9. Numbers: Spell out numbers one through nine, use figures for 10 and above (with exceptions as per AP style)
    
    10. State names: Spell out state names in the body of the article, use AP style abbreviations in datelines
    
    11. Titles and names: Use proper capitalization and formatting for titles before names, lowercase titles after names or standing alone
    
    12. Abbreviations and acronyms: Spell out on first reference, followed by the acronym in parentheses. Use the acronym for subsequent references.
    
    13. Avoid unnecessary stylistic flourishes. Use em dashes, rhetorical questions, and one-sentence paragraphs sparingly for emphasis.
    
    14. Dateline: Include a proper AP style dateline at the beginning of the article if the story is from a specific location.
    
    Produce a factual, objective news article adhering to these AP style guidelines and journalistic best practices."""
        
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
