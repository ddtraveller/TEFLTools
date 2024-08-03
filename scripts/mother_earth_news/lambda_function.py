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

# Load dictionary contents
with open('dictionary.json', 'r', encoding='utf-8') as f:
    DICT_FILE = f.read()
with open('phrases.json', 'r', encoding='utf-8') as f:
    PHRASES_FILE = f.read()
with open('compound.json', 'r', encoding='utf-8') as f:
    COMPOUND_FILE = f.read()

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

def translate_english_to_tetun(text, anthropic_client):
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
    
    Dictionary: {DICT_FILE}
    Phrases: {PHRASES_FILE}
    Compound words: {COMPOUND_FILE}
    
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