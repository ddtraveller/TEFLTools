import boto3
from bs4 import BeautifulSoup
import re
from gtts import gTTS
from io import BytesIO
import os
from urllib.parse import urlparse

# Initialize S3 client
s3 = boto3.client('s3')

def get_s3_file(url):
    parsed_url = urlparse(url)
    bucket = parsed_url.netloc.split('.')[0]
    key = parsed_url.path.lstrip('/')
    response = s3.get_object(Bucket=bucket, Key=key)
    html_content = response['Body'].read().decode('utf-8')
    return html_content, bucket, key

def parse_html_for_audio(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    audio_data = []
    for div in soup.find_all('div', class_='story-part'):
        part_number = div.find('h2').text.strip()
        text = div.find('p').text.strip()
        audio_tag = div.find('audio')
        if audio_tag and audio_tag.find('source'):
            audio_url = audio_tag.find('source')['src']
            audio_filename = audio_url.split('/')[-1]
            audio_data.append({
                'part': part_number,
                'text': text,
                'filename': audio_filename
            })
    return audio_data, soup

def generate_sound(text, filename, bucket):
    # Replace apostrophes with empty strings
    text = text.replace("'", "")
    text = re.sub(r'Part \d+$', '', text).strip()
    
    # Create a gTTS object with the given text and language
    tts = gTTS(text=text, lang='en', tld='co.uk')
    
    # Create a BytesIO object to store the audio data
    fp = BytesIO()
    
    # Write the audio data to the BytesIO object
    tts.write_to_fp(fp)
    
    # Move the file pointer to the beginning of the BytesIO object
    fp.seek(0)
    
    # Save the audio data to S3
    s3.put_object(
        Bucket=bucket,
        Key=f'sounds/{filename}',
        Body=fp,
        ContentType='audio/mpeg'
    )
    
    return f'https://{bucket}.s3.us-west-2.amazonaws.com/sounds/{filename}'

def update_html(soup, audio_data):
    for item in audio_data:
        div = soup.find('div', class_='story-part', string=lambda text: item['part'] in text)
        if div:
            audio_tag = div.find('audio')
            if audio_tag:
                source_tag = audio_tag.find('source')
                if source_tag:
                    source_tag['src'] = f'sounds/{item["filename"]}'
    return str(soup)

def main():
    # Prompt for S3 file location
    s3_url = input("Enter the S3 file URL (e.g., https://tl-web.s3.us-west-2.amazonaws.com/stories/bedtime_1723965739.html): ")
    
    # Get the HTML content and S3 details
    html_content, bucket, key = get_s3_file(s3_url)
    
    # Parse the HTML to extract audio data
    audio_data, soup = parse_html_for_audio(html_content)
    
    # Generate and replace sound files
    for item in audio_data:
        print(f"Generating new audio for {item['part']}")
        new_audio_url = generate_sound(item['text'], item['filename'], bucket)
        print(f"New audio file generated and uploaded: {new_audio_url}")
    
    # Update the HTML content
    updated_html = update_html(soup, audio_data)
    
    # Upload the updated HTML back to S3
    s3.put_object(Bucket=bucket, Key=key, Body=updated_html, ContentType='text/html')
    
    print(f"Updated HTML file has been uploaded back to S3: {s3_url}")

if __name__ == "__main__":
    main()