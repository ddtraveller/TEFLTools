import os
import boto3
import json
import requests
from bs4 import BeautifulSoup
import base64
from io import BytesIO
import re
import time

# Initialize AWS client
s3 = boto3.client('s3')

# Get the Stability API key from an environment variable
stability_api_key = os.getenv('STABILITY_API_KEY')

# Check if the API key is set
if stability_api_key is None:
    raise ValueError("The STABILITY_API_KEY environment variable is not set.")

def invalidate_cloudfront_cache(distribution_id, story_name):
    cloudfront_client = boto3.client('cloudfront')
    
    invalidation_batch = {
        'Paths': {
            'Quantity': 1,
            'Items': [f'/images/{story_name}*']
        },
        'CallerReference': str(hash(story_name))  # Unique string for this invalidation
    }
    
    try:
        response = cloudfront_client.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch=invalidation_batch
        )
        print(f"Invalidation created successfully. ID: {response['Invalidation']['Id']}")
    except Exception as e:
        print(f"Error creating invalidation: {str(e)}")

def get_s3_file_content(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    file_content = response['Body'].read().decode('utf-8')
    return file_content

def parse_images_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    images = soup.find_all('img')
    return [img['src'] for img in images]

def generate_new_image(payload, reference_image=None):
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "Accept": "image/*",
        "Authorization": f"Bearer {stability_api_key}"
    }
    
    files = {
        "prompt": (None, payload["prompt"]),
        "negative_prompt": (None, payload.get("negative_prompt", "")),
        "output_format": (None, "png"),
        "cfg_scale": (None, str(payload["cfg_scale"])),
        "clip_guidance_preset": (None, payload["clip_guidance_preset"]),
        "height": (None, str(payload["height"])),
        "width": (None, str(payload["width"])),
        "samples": (None, str(payload["samples"])),
        "steps": (None, str(payload["steps"])),
        "style_preset": (None, payload["style_preset"]),
        "seed": (None, str(payload["seed"]))
    }
    
    if reference_image:
        files["image"] = ("reference.png", reference_image, "image/png")
        files["strength"] = (None, "0.35")
        files["mode"] = (None, "image-to-image")
    
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, files=files)
            response.raise_for_status()
            
            if response.headers['Content-Type'].startswith('image/'):
                return BytesIO(response.content)
            else:
                raise Exception(f"Unexpected content type: {response.headers['Content-Type']}")
        except requests.exceptions.RequestException as e:
            print(f"Error generating image on attempt {attempt + 1}: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response content: {e.response.content}")
            
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"Failed to generate image after {max_retries} attempts.")
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

def generate_story_image(part, style, is_first_image, reference_image=None):
    story_instruction = f"Create a child-friendly {style} illustration."
    
    style_prompt = """
    Use a vibrant, colorful palette reminiscent of Jaime Hernandez's work in Love and Rockets.
    Character designs should blend realistic proportions with slightly exaggerated features, similar to Wendy Pini's elves in Elfquest.
    Architecture should be gigantic, whimsical, ultra technical or magical or cosmic. Very comic book. 
    Flora and fauna should me mythical, magical, diverse and local to Timor Leste.
    Include details that reflect Timorese culture, such as traditional tais textiles, uma lulik (sacred houses), local flora and fauna, and Inan Nunu; the Divine Mother who nourishes all in this land.
    Mix ultra post-modern and ancient anachronistic elements to create a unique, futuristic Timorese aesthetic.
    Use dynamic compositions and dramatic angles inspired by comic book panels.
    Incorporate subtle magical or fantastical elements that blend seamlessly with the realistic setting.
    Emphasize expressive character faces and body language to convey emotions.
    Use lighting effects to create mood and atmosphere, especially for scenes set at different times of day.    
    Use a vibrant, bold color palette with rich, saturated hues, particularly emphasizing warm oranges, deep teals, and lush greens.
    Employ a comic book or graphic novel art style with clean, defined outlines and flat colors.
    Create detailed, fantastical backgrounds that blend natural elements (like the mushroom-like trees) with cosmic imagery (planets and stars).
    Use perspective to create a sense of wonder, such as positioning the viewer to look up at towering flora or celestial objects.
    Incorporate small, whimsical details like floating particles or small creatures to add life to the scene.
    Ensure character clothing is simple yet modern, with solid colors that stand out against the busy background.
    Use subtle gradients and shading to add dimension to flat color areas, especially on larger objects like planets.
    """    

    consistency_prompt = "Create a consistent style for the story." if is_first_image else "Maintain style consistency with previous illustrations."

    prompt = f"{story_instruction} {part} {style_prompt} {consistency_prompt}"

    payload = {
        "prompt": prompt,
        "cfg_scale": 15,
        "clip_guidance_preset": "FAST_BLUE",
        "height": 576,
        "width": 1024,
        "samples": 1,
        "steps": 50,
        "style_preset": style,
        "seed": 3594967295
    }

    return generate_new_image(payload, reference_image)

def parse_s3_location(s3_input):
    # Check if it's an ARN
    arn_match = re.match(r'arn:aws:s3:::([^/]+)/(.+)', s3_input)
    if arn_match:
        return arn_match.group(1), arn_match.group(2)
    
    # Check if it's an S3 URL
    url_match = re.match(r's3://([^/]+)/(.+)', s3_input)
    if url_match:
        return url_match.group(1), url_match.group(2)
    
    # If it's neither, assume it's a direct path
    parts = s3_input.split('/', 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    
    raise ValueError("Invalid S3 location format")

def get_reference_image():
    s3_input = input("Enter the S3 ARN, URL, or path for the reference image (or press Enter to skip): ")
    if s3_input:
        try:
            bucket, key = parse_s3_location(s3_input)
            response = s3.get_object(Bucket=bucket, Key=key)
            return BytesIO(response['Body'].read())
        except Exception as e:
            print(f"Error getting reference image: {str(e)}")
    return None

def main():
    # Prompt for S3 file location
    bucket = 'tl-web'
    key = input("Enter the S3 file key of the story: ")

    # Get content of the specified S3 file
    html_content = get_s3_file_content(bucket, key)
    
    # Parse current image URLs from HTML
    current_image_urls = parse_images_from_html(html_content)
    
    # Prompt for story name
    story_name = input("Enter the story name for CloudFront invalidation: ")
    
    # Prompt for replacing all images or a single image
    replace_all = input("Do you want to replace all images? (y/n): ").lower() == 'y'

    # Get reference image
    reference_image = get_reference_image()

    if replace_all:
        style = input("Enter the style preset for all images: ")
        for part_number in range(6):  # 0 to 5
            part = input(f"Enter the story part description for image {part_number}: ")
            is_first_image = part_number == 0
            new_image = generate_story_image(part, style, is_first_image, reference_image if part_number == 0 else None)
            replace_image(current_image_urls[part_number], new_image)
            print(f"Image {part_number} replaced")
    else:
        # Original single image replacement logic
        part_number = int(input("Enter the part number (0-5): "))
        part = input("Enter the story part description: ")
        style = input("Enter the style preset: ")
        is_first_image = input("Is this the first image? (y/n): ").lower() == 'y'
        
        new_image = generate_story_image(part, style, is_first_image, reference_image)
        
        if 0 <= part_number < len(current_image_urls):
            replace_image(current_image_urls[part_number], new_image)
        else:
            print("Invalid part number. No image was replaced.")
    
    print("Image generation and replacement complete")
    # Perform CloudFront invalidation
    invalidate_cloudfront_cache('EA9FU4A37EB95', story_name)

if __name__ == "__main__":
    main()