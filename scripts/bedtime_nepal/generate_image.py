import os
import requests
from io import BytesIO
from PIL import Image

# Get the Stability API key from an environment variable
stability_api_key = os.getenv('STABILITY_API_KEY')

# Check if the API key is set
if stability_api_key is None:
    raise ValueError("The STABILITY_API_KEY environment variable is not set.")

def get_reference_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = img.convert('RGB')
        img = img.resize((1024, 1024))  # Resize to 1024x1024
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        return img_byte_arr
    except requests.exceptions.RequestException as e:
        print(f"Error getting reference image: {str(e)}")
        return None

def generate_new_image(prompt, reference_image=None):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image"
    headers = {
        "Accept": "image/png",  # Changed this line
        "Authorization": f"Bearer {stability_api_key}"
    }
    
    files = {
        "init_image": ("reference.png", reference_image, "image/png") if reference_image else None,
        "text_prompts[0][text]": (None, prompt),
        "text_prompts[0][weight]": (None, "1"),
        "cfg_scale": (None, "7"),
        "clip_guidance_preset": (None, "FAST_BLUE"),
        "samples": (None, "1"),
        "steps": (None, "30"),
    }
    
    if reference_image:
        files["image_strength"] = (None, "0.26")

    response = requests.post(url, headers=headers, files={k: v for k, v in files.items() if v is not None})
    
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
    
    return None

def save_image(image, filename):
    with open(filename, 'wb') as f:
        f.write(image.getvalue())
    print(f"Image saved as {filename}")

def main():
    description = input("Enter the image description: ")
    ref_image_url = input("Enter the HTTPS URL for the reference image (or press Enter to skip): ")

    reference_image = None
    if ref_image_url:
        reference_image = get_reference_image(ref_image_url)

    new_image = generate_new_image(description, reference_image)

    if new_image:
        save_image(new_image, "generated_image.png")
    else:
        print("Failed to generate image.")

if __name__ == "__main__":
    main()