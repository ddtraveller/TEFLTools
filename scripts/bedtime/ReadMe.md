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

## Note

This project requires API keys for Anthropic and Stability AI, as well as Google Cloud credentials for the Text-to-Speech API. Ensure these are securely stored and never committed to version control.