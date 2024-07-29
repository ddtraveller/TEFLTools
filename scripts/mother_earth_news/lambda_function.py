import json
import os
import requests
from anthropic import Anthropic
import boto3
from datetime import datetime
import tiktoken

# Constants
TOPICS = [
    "Timor-Leste spirituality, holistic healing, permaculture",
    "Notísia husi Timor-Leste"
]
API_KEY = os.environ['GOOGLE_API_KEY']
SEARCH_ENGINE_ID = os.environ['SEARCH_ENGINE_ID']
ANTHROPIC_API_KEY = os.environ['ANTHROPIC_API_KEY']
S3_BUCKET = os.environ['S3_BUCKET']

# Initialize clients
anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY)
s3 = boto3.client('s3')

# Load dictionary, phrases, and compounds (You'll need to implement this part)
english_to_tetun = {}  # Load this from your dictionary file
tetun_phrases = {}  # Load this from your phrases file
tetun_compounds = {}  # Load this from your compounds file

def lambda_handler(event, context):
    all_results = []
    
    for topic in TOPICS:
        results = search_topic(topic)
        commentary = get_commentary(topic, results)
        translated_commentary = translate_english_to_tetun(commentary, anthropic_client)
        all_results.append({
            'topic': topic,
            'results': results,
            'commentary': commentary,
            'translated_commentary': translated_commentary
        })
    
    html_content = generate_html(all_results)
    
    # Save results to S3
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f'mnews_{timestamp}.html'
    
    # Check if mnews.html exists and rename it
    try:
        s3.head_object(Bucket=S3_BUCKET, Key='mnews.html')
        old_file_name = f"mnews_{datetime.now().strftime('%m%d%Y')}.html"
        s3.copy_object(
            Bucket=S3_BUCKET,
            CopySource={'Bucket': S3_BUCKET, 'Key': 'mnews.html'},
            Key=old_file_name
        )
        s3.delete_object(Bucket=S3_BUCKET, Key='mnews.html')
    except:
        pass
    
    # Save to the original bucket
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=file_name,
        Body=html_content,
        ContentType='text/html'
    )
    
    # Copy to tl-web bucket as mnews.html
    s3.copy_object(
        CopySource={'Bucket': S3_BUCKET, 'Key': file_name},
        Bucket='tl-web',
        Key='mnews.html'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Processing complete. Results saved to S3 as {file_name} and copied to tl-web bucket as mnews.html')
    }

def search_topic(topic):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'cx': SEARCH_ENGINE_ID,
        'key': API_KEY,
        'q': topic,
        'num': 5
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    results = []
    for item in data.get('items', []):
        results.append({
            'title': item.get('title', ''),
            'link': item.get('link', ''),
            'snippet': item.get('snippet', '')
        })
    
    return results

def get_commentary(topic, results):
    prompt = f"Human: Based on the following articles about {topic}, please provide a commentary from a non-dual, spiritual perspective that emphasizes the interconnectedness of all life and encourages living in loving harmony with mother nature. Do not include any introductory text before the actual commentary, such as 'Here is a suggested commentary' or similar phrases. Start the response directly with the commentary text:\n\n"
    
    for result in results:
        prompt += f"Title: {result['title']}\nLink: {result['link']}\nSnippet: {result['snippet']}\n\n"
    
    prompt += "Assistant:"
    
    response = anthropic_client.completions.create(
        prompt=prompt,
        model="claude-v1",
        max_tokens_to_sample=1000,
        stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
    )
    
    return response.completion.strip()

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def translate_words(text, dictionary):
    words = text.split()
    translated_words = []
    for word in words:
        # Convert to lowercase for dictionary lookup
        lower_word = word.lower()
        # Check if the word or its lemma (if different) is in the dictionary
        if lower_word in dictionary:
            translated_words.append(dictionary[lower_word])
        else:
            # If not found, keep the original word
            translated_words.append(word)
    return ' '.join(translated_words)

def preprocess_text(text):
    # Implement preprocess_tetun_word_order, translate_aspect_markers, 
    # translate_pronouns, translate_compounds, and handle_reduplication here
    return text

def get_best_tetun_words(english_word, cfd, n=5):
    if english_word in cfd.conditions(): 
        return cfd[english_word].most_common(n)
    else:
        return []

def translate_english_to_tetun(text, anthropic_client):
    # Simple word-by-word translation
    words = text.split()
    translated_words = [english_to_tetun.get(word.lower(), word) for word in words]
    initial_translation = ' '.join(translated_words)
    
    # Use Anthropic's API for final translation
    prompt = f"Human: Translate the following English text to Tetun, keeping in mind Tetun grammar rules:\n\n{initial_translation}\n\nTetun translation:\n\nAssistant:"
    
    response = anthropic_client.completions.create(
        prompt=prompt,
        model="claude-v1",
        max_tokens_to_sample=1000,
        stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
    )
    
    return response.completion.strip()

def generate_html(results):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Notísia husi Timor-Leste</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }
            h1 { color: #2c3e50; }
            h2 { color: #34495e; }
            .topic { margin-bottom: 40px; }
            .article { margin-bottom: 20px; }
            .article h3 { margin-bottom: 5px; }
            .article a { color: #3498db; text-decoration: none; }
            .article a:hover { text-decoration: underline; }
            .commentary { background-color: #f9f9f9; padding: 15px; border-radius: 5px; }
        </style>
    </head>
    <body>
    """
    
    for result in results:
        html += f"""
        <div class="topic">
            <h2>{result['topic']}</h2>
            <div class="articles">
                <h3>Artigu sira-ne'ebé relasiona:</h3>
        """
        
        for article in result['results']:
            html += f"""
                <div class="article">
                    <h3><a href="{article['link']}" target="_blank">{article['title']}</a></h3>
                    <p>{article['snippet']}</p>
                </div>
            """
        
        html += f"""
            </div>
            <div class="commentary">
                <h3>Komentáriu Tetun:</h3>
                <p>{result['translated_commentary']}</p>
                <h3>English Commentary:</h3>
                <p>{result['commentary']}</p>
            </div>
        </div>
        """
    
    html += """
    </body>
    </html>
    """
    
    return html