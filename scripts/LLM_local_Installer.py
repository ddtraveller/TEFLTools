import os
import requests
from tqdm import tqdm

def download_file(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as progress_bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            progress_bar.update(size)

def main():
    # Dictionary of available models and their download URLs
    models = {
        "1": {
            "name": "GPT4All Falcon",
            "url": "https://gpt4all.io/models/ggml-gpt4all-falcon-q4_0.bin"
        },
        "2": {
            "name": "Replit Code V1.5 3B Q4_0",
            "url": "https://gpt4all.io/models/ggml-replit-code-v1-3b.bin"
        },
        "3": {
            "name": "Llama 2 Uncensored",
            "url": "https://gpt4all.io/models/ggml-llama-2-7b-uncensored.bin"
        }
    }

    print("Available GPT4All models:")
    for key, model in models.items():
        print(f"{key}. {model['name']}")

    choice = input("Enter the number of the model you want to install: ")

    if choice not in models:
        print("Invalid choice. Exiting.")
        return

    model = models[choice]
    model_name = model['name']
    model_url = model['url']

    # Create a directory for the models if it doesn't exist
    os_name = os.name
    if os_name == 'nt':  # Windows
        model_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'nomic.ai', 'GPT4All')
    elif os_name == 'posix':  # macOS and Linux
        model_dir = os.path.join(os.path.expanduser('~'), '.local', 'share', 'nomic.ai', 'GPT4All')
    else:
        print(f"Unsupported operating system: {os_name}")
        return

    os.makedirs(model_dir, exist_ok=True)

    # Download the model
    model_path = os.path.join(model_dir, os.path.basename(model_url))
    print(f"Downloading {model_name} to {model_path}")
    download_file(model_url, model_path)

    print(f"\nModel downloaded successfully to: {model_path}")
    print("You can now use this path in your GPT4All scripts.")

if __name__ == "__main__":
    main()