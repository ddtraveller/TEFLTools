import os
import boto3
import json
import requests
from bs4 import BeautifulSoup
import base64
from io import BytesIO

# Initialize AWS client
s3 = boto3.client('s3')

# Get the Stability API key from an environment variable
stability_api_key = os.getenv('STABILITY_API_KEY')

# Check if the API key is set
if stability_api_key is None:
    raise ValueError("The STABILITY_API_KEY environment variable is not set.")

def get_bedtime_html():
    response = s3.get_object(Bucket='tl-web', Key='bedtime.html')
    html_content = response['Body'].read().decode('utf-8')
    return html_content

def parse_images_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    images = soup.find_all('img')
    return [img['src'] for img in images]

def generate_new_image(payload):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {stability_api_key}"
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        data = response.json()
        if "artifacts" in data and len(data["artifacts"]) > 0:
            image_data = base64.b64decode(data["artifacts"][0]["base64"])
            return BytesIO(image_data)
        else:
            print(f"No image data in response for payload: {payload}")
            return None
    except requests.exceptions.HTTPError as e:
        print(f"Error generating image for payload: {payload}")
        print(f"HTTP error: {e}")
        return None

def replace_image(url, new_image):
    if new_image is None:
        print(f"Skipping image replacement for URL: {url}")
        return
    
    # Extract the image name from the URL
    image_name = url.split('/')[-1]
    
    # Upload the new image to S3
    s3.put_object(
        Bucket='tl-web',
        Key=f'images/{image_name}',
        Body=new_image.getvalue(),
        ContentType='image/png'
    )
    print(f"Replaced image: {image_name}")

def generate_story_image(part, style, is_first_image):
    story_instruction = f"Create a whimsical, child-friendly {style} illustration for a bedtime story."
    culture_prompt = "Make sure all people depicted look like people from Timor Leste. They should have brown skin. They should not be caucasian."
    consistency_prompt = "Create a consistent style for the story." if is_first_image else "Maintain style consistency with previous illustrations."

    payload = {
        "text_prompts": [
            {"text": story_instruction, "weight": 1.2},
            {"text": part, "weight": 1},
            {"text": culture_prompt, "weight": 0.75},
            {"text": consistency_prompt, "weight": 1.5},
        ],
        "cfg_scale": 15,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 576,
        "width": 1024,
        "samples": 1,
        "steps": 50,
        "style_preset": style,
        "seed": 3194967295
    }

    return generate_new_image(payload)

def main():
    # Get current bedtime.html content
    html_content = get_bedtime_html()
    
    # Parse current image URLs from HTML
    current_image_urls = parse_images_from_html(html_content)
    
    # Prompt for user input
    part_number = int(input("Enter the part number (0-5): "))
    part = input("Enter the story part description: ")
    style = input("Enter the style preset: ")
    is_first_image = input("Is this the first image? (y/n): ").lower() == 'y'
    
    # Generate new image based on user input
    new_image = generate_story_image(part, style, is_first_image)
    
    # Replace the specified image in S3
    if 0 <= part_number < len(current_image_urls):
        replace_image(current_image_urls[part_number], new_image)
    else:
        print("Invalid part number. No image was replaced.")
    
    print("Image generation and replacement complete")

if __name__ == "__main__":
    main()