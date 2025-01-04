# Bedtime Story Generator

This project is an AWS Lambda function that generates bedtime stories in both English and Tetun, complete with illustrations and audio narration.

## Overview

The Bedtime Story Generator uses AI to create unique, culturally-appropriate stories for children in Timor-Leste. It leverages several APIs and services to produce a complete multimedia story experience.

## Key Components

1. **Story Generation**: Uses Anthropic's API to create original stories.
2. **Image Generation**: Employs Stability AI's API to create illustrations for each story part.
3. **Text-to-Speech**: Utilizes Google's Text-to-Speech API to generate audio narrations.
4. **Language Translation**: Translates stories from English to Tetun using a custom dictionary and grammar rules.
5. **AWS Integration**: Runs on AWS Lambda and uses S3 for storage.

## How It Works

1. **Story Creation**:
   - A random seed and cultural context are selected.
   - The Anthropic API generates a story based on these inputs.
   - The story is parsed into separate parts (title, introduction, rising action, climax, resolution).

2. **Translation**:
   - The English story is translated to Tetun using a custom dictionary and Tetun grammar rules.
   - This process ensures culturally appropriate and grammatically correct translations.

3. **Image Generation**:
   - For each story part, a prompt is created and sent to the Stability AI API.
   - The API returns an image that visually represents that part of the story.

4. **Audio Generation**:
   - The English text for each part is converted to speech using Google's Text-to-Speech API.

5. **HTML Generation**:
   - An HTML page is created, combining the story text (in both languages), images, and audio files.

6. **Storage and Hosting**:
   - All generated content (HTML, images, audio) is uploaded to an AWS S3 bucket.

## Key Functions

- `generate_story()`: Creates the story using the Anthropic API.
- `generate_image()`: Produces illustrations using the Stability AI API.
- `generate_sound()`: Creates audio narrations using Google's Text-to-Speech.
- `generate_html()`: Assembles all components into a single HTML page.

## Language Translation

The translation process uses a combination of:
- A custom English-to-Tetun dictionary (`dictionary.json`)
- Tetun phrases (`phrases.json`)
- Compound words (`compound.json`)
- Tetun grammar rules implemented in the code

This ensures that the translations are not just word-for-word, but follow proper Tetun language structure and idioms.

## Setup and Deployment

The project includes a bash script (`deploy.sh`) that automates the process of creating and updating the AWS Lambda function. This script:

1. Sets up the necessary IAM roles and policies.
2. Packages the Lambda function code and dependencies.
3. Creates or updates the Lambda function in AWS.
4. Sets environment variables for API keys.

To deploy:
1. Ensure you have the AWS CLI configured with appropriate permissions.
2. Run `./deploy.sh` from the project directory.
3. Follow the prompts to input API keys if not already set as environment variables.

## Dependencies

- Python 3.9
- AWS SDK (Boto3)
- Anthropic Python SDK
- Requests library
- Tiktoken (for token counting)
- gTTS (Google Text-to-Speech)
- Lark (for parsing)

These dependencies are automatically installed in the Lambda environment by the deployment script.

## Detailed API Call Configurations

### 1. Anthropic API (Story Generation)

The Anthropic API is used to generate the original story content. Here's a detailed breakdown of the API call:

```python
response = anthropic_client.completions.create(
    prompt=prompt,
    model="claude-v1",
    max_tokens_to_sample=7000,
    stop_sequences=["\n\nHuman:", "\n\nAssistant:"]
)
```

- **Client**: The `anthropic_client` is initialized using the Anthropic Python SDK.
- **Method**: `completions.create` is used to generate text completions.
- **Parameters**:
  - `prompt`: A string containing the story prompt, cultural context, and any additional instructions.
  - `model`: Set to "claude-v1", which is Anthropic's large language model.
  - `max_tokens_to_sample`: Set to 7000, allowing for lengthy story generation.
  - `stop_sequences`: Defines sequences that will stop the generation if encountered.

The API key is set as an environment variable `ANTHROPIC_API_KEY` in the Lambda function configuration.

### 2. Stability AI API (Image Generation)

The Stability AI API is used to generate illustrations for each part of the story. Here's a detailed look at the API call:

```python
url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {stability_api_key}"
}
payload = {
    "text_prompts": [
        {"text": story_instruction, "weight": 1.2},
        {"text": part, "weight": 1},
        {"text": full_story, "weight": 0.75},
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
response = requests.post(url, headers=headers, json=payload)
```

- **Endpoint**: Uses the text-to-image generation endpoint of Stability AI's API.
- **Headers**: 
  - Content-Type and Accept are set to "application/json".
  - Authorization uses a bearer token (the Stability AI API key).
- **Payload**:
  - `text_prompts`: An array of prompts with associated weights to guide the image generation.
  - `cfg_scale`: Set to 15, controlling how closely the image follows the prompt. 1-20
  - `clip_guidance_preset`: Set to "FAST_BLUE" for quicker generation.
  - `height` and `width`: Define the image dimensions.
  - `samples`: Set to 1, generating one image per request.
  - `steps`: Set to 50, defining the number of diffusion steps. 50 max.
  - `style_preset`: Varies based on the story context.
  - `seed`: A fixed seed for reproducibility.

The API key is stored as an environment variable `STABILITY_API_KEY` in the Lambda function.

### 3. Google Text-to-Speech API (Audio Generation)

The Google Text-to-Speech API is used to create audio narrations. Here's how it's configured:

```python
tts = gTTS(text=text, lang='en', tld='co.uk')
fp = BytesIO()
tts.write_to_fp(fp)
```

- **Library**: Uses the `gTTS` (Google Text-to-Speech) Python library, which interfaces with Google's API.
- **Parameters**:
  - `text`: The story text to be converted to speech.
  - `lang`: Set to 'en' for English.
  - `tld`: Set to 'co.uk' to use a UK English voice.
- **Output**: The audio is written to a BytesIO object, which can then be saved or uploaded.

The Google Cloud credentials are stored as an environment variable `GOOGLE_CREDENTIALS` in the Lambda function, encoded in base64.

### 4. AWS S3 (Storage and Hosting)

AWS S3 is used to store and host the generated content. Here's an example of how files are uploaded to S3:

```python
s3.put_object(
    Bucket='tl-web',
    Key=f'images/{image_name}',
    Body=image_data.getvalue(),
    ContentType='image/png'
)
```

- **Client**: The `s3` client is initialized using boto3, the AWS SDK for Python.
- **Method**: `put_object` is used to upload files to S3.
- **Parameters**:
  - `Bucket`: The name of the S3 bucket ('tl-web' in this case).
  - `Key`: The path and filename within the bucket.
  - `Body`: The content of the file.
  - `ContentType`: The MIME type of the file.

AWS credentials are managed through IAM roles assigned to the Lambda function, eliminating the need for explicit API keys.

These API configurations allow the Lambda function to seamlessly integrate multiple services to generate, translate, illustrate, narrate, and host the bedtime stories.

### 5. Lambda
You can pass in an event like this at the lambda console in a test or call the lambda with a payload with a structure like this that will replace the random_element story seed.
{
  "story_seed": "Title: The Lady with the Tais\n\nIn the tranquil seaside city of Dili, Timor-Leste, João Santos, a married civil servant from Baucau, encounters Maria da Costa, a young woman wearing a vibrant tais and walking along the beach. Despite his usual indifference towards fleeting encounters, João is captivated by Maria's grace and the melancholy in her eyes. They strike up a conversation, and soon find themselves drawn into a passionate affair, initially viewing it as a brief escape from their everyday lives. As they spend time together, exploring Dili's colonial Portuguese architecture and pristine beaches, their connection deepens, transcending physical attraction. When Maria returns to her hometown of Suai, João is surprised by the void her absence creates. Driven by an inexplicable longing, he travels to Suai, where he spots her at a traditional tebe dance ceremony. Their reunion is intense and emotional, forcing them to confront the depth of their feelings. They continue their clandestine relationship, meeting occasionally in Dili, their rendezvous colored by the city's blend of Timorese tradition and post-independence aspirations. As the story concludes, João and Maria find themselves entangled in a complex web of love, duty, and societal expectations, set against the backdrop of Timor-Leste's rich culture and recent history of struggle and resilience. They face an uncertain future, their personal dilemma mirroring the nation's own journey of self-discovery and reconciliation."
}