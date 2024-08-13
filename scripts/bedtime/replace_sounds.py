import boto3
from bs4 import BeautifulSoup
import re
from gtts import gTTS
from io import BytesIO
import os

# Initialize S3 client
s3 = boto3.client('s3')

def get_bedtime_html():
    response = s3.get_object(Bucket='tl-web', Key='bedtime.html')
    html_content = response['Body'].read().decode('utf-8')
    return html_content

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

    return audio_data

def generate_sound(text, filename):
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
        Bucket='tl-web',
        Key=f'sounds/{filename}',
        Body=fp,
        ContentType='audio/mpeg'
    )
    
    return f'https://tl-web.s3.us-west-2.amazonaws.com/sounds/{filename}'

def main():
    # Get the bedtime.html content
    html_content = get_bedtime_html()
    
    # Parse the HTML to extract audio data
    audio_data = parse_html_for_audio(html_content)
    
    # Generate and replace sound files
    for item in audio_data:
        print(f"Generating new audio for {item['part']}")
        new_audio_url = generate_sound(item['text'], item['filename'])
        print(f"New audio file generated and uploaded: {new_audio_url}")

    print("All sound files have been replaced successfully.")

if __name__ == "__main__":
    main()