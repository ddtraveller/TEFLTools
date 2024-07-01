import os
import re
import requests
import anthropic
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time

# Initialize the Anthropic client
client = anthropic.Anthropic()

def clean_filename(filename):
    """Clean the filename to be safe for file systems."""
    return re.sub(r'[^\w\-_\. ]', '_', filename)

def fetch_and_clean_url_content(url):
    """Fetch content from URL and clean it using Anthropic."""
    try:
        print(f"Fetching content from URL: {url}")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text content
        text_content = soup.get_text()
        print(f"Extracted {len(text_content)} characters from the URL")
        
        # Use Anthropic to clean and format the content
        prompt = f"Clean and format the following text content from a webpage, removing any irrelevant information and preserving only the main text content:\n\n{text_content[:2000]}..."  # Limit to 2000 chars for API

        print("Sending request to Anthropic for content cleaning...")
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2000,
            temperature=0,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        time.sleep(5)  # Pause for 5 seconds after Anthropic call
        cleaned_content = message.content[0].text if message.content else ""
        print(f"Received cleaned content from Anthropic ({len(cleaned_content)} characters)")
        return cleaned_content
    except Exception as e:
        print(f"Error fetching or cleaning URL content: {str(e)}")
        return process_error_with_anthropic(url)

def process_error_with_anthropic(resource):
    """Process errors by asking Anthropic to provide an excerpt or summary."""
    prompt = f"I encountered an error while trying to access the following resource: {resource}. Can you please provide a brief summary or excerpt of what this resource might contain, based on its title or description?"

    try:
        print(f"Sending error handling request to Anthropic for: {resource}")
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0.2,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        time.sleep(5)  # Pause for 5 seconds after Anthropic call
        processed_content = message.content[0].text if message.content else ""
        print(f"Received error handling content from Anthropic ({len(processed_content)} characters)")
        return processed_content
    except Exception as e:
        print(f"Error in error handling process: {str(e)}")
        return ""

def process_resource_request(week_name, request):
    """Process a resource request using Anthropic."""
    prompt = f"For a fiction writing course in {week_name}, please {request}"

    try:
        print(f"Sending resource request to Anthropic: {request}")
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2000,
            temperature=0.2,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        time.sleep(5)  # Pause for 5 seconds after Anthropic call
        processed_content = message.content[0].text if message.content else ""
        print(f"Received processed content from Anthropic ({len(processed_content)} characters)")
        return processed_content
    except Exception as e:
        print(f"Error processing resource request: {str(e)}")
        return ""

def process_additional_resource(week_name, resource):
    """Process an additional resource using Anthropic."""
    if '[Link to audio' in resource or '[Link to video' in resource:
        prompt = f"For a fiction writing course in {week_name}, please provide a text-based alternative or transcript for the following audio/video resource: {resource}"
    elif resource.startswith('[') and resource.endswith(']'):
        prompt = f"For a fiction writing course in {week_name}, please create or find content related to: {resource}"
    else:
        prompt = f"For a fiction writing course in {week_name}, please create a comprehensive resource on the following topic: {resource}"

    try:
        print(f"Sending additional resource request to Anthropic: {resource}")
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=3000,
            temperature=0.2,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        time.sleep(5)  # Pause for 5 seconds after Anthropic call
        processed_content = message.content[0].text if message.content else ""
        print(f"Received processed content from Anthropic ({len(processed_content)} characters)")
        return processed_content
    except Exception as e:
        print(f"Error processing additional resource: {str(e)}")
        return ""

def process_file(filename):
    """Process a single lesson resource file."""
    print(f"Processing file: {filename}")
    with open(filename, 'r') as file:
        content = file.read()

    print(f"File content length: {len(content)} characters")

    # Extract week name from content
    week_name_match = re.search(r'### Week (\d+(-\d+)?)', content)
    if week_name_match:
        week_name = week_name_match.group(0)
    else:
        week_name = os.path.splitext(filename)[0]
    print(f"Week name: {week_name}")

    # Find the Additional Resources section
    additional_resources_section = re.search(r'## Additional Resources\s*([\s\S]*?)(?=\n#|$)', content)
    
    if additional_resources_section:
        resources = re.findall(r'- (.+)', additional_resources_section.group(1))
        print(f"Found {len(resources)} additional resources")
        
        for resource in resources:
            print(f"Processing additional resource: {resource}")
            
            if resource.startswith('[') and '](' in resource and resource.endswith(')'):
                # This is a Markdown link
                link_text, url = re.match(r'\[(.*?)\]\((.*?)\)', resource).groups()
                print(f"Processing URL: {url}")
                cleaned_content = fetch_and_clean_url_content(url)
                if cleaned_content:
                    output_filename = f"{clean_filename(week_name)}_{clean_filename(link_text)}.txt"
                    with open(output_filename, 'w') as out_file:
                        out_file.write(cleaned_content)
                    print(f"Wrote cleaned content to {output_filename}")
            elif resource.startswith('[') and resource.endswith(']'):
                # This is a resource request in square brackets
                request = resource[1:-1]  # Remove square brackets
                processed_content = process_resource_request(week_name, request)
                if processed_content:
                    output_filename = f"{clean_filename(week_name)}_resource_{clean_filename(request)}.md"
                    with open(output_filename, 'w') as out_file:
                        out_file.write(processed_content)
                    print(f"Wrote resource request content to {output_filename}")
            else:
                # This is a regular resource (like a book title)
                processed_content = process_additional_resource(week_name, resource)
                if processed_content:
                    key = '_'.join(resource.split()[:3]).lower()
                    output_filename = f"{clean_filename(week_name)}_additional_{clean_filename(key)}.md"
                    with open(output_filename, 'w') as out_file:
                        out_file.write(processed_content)
                    print(f"Wrote additional resource content to {output_filename}")
    else:
        print("No Additional Resources section found")
        
def main():
    start_week = input("Enter the week number to start processing (default is 1): ")
    try:
        start_week = int(start_week)
    except ValueError:
        print("Invalid input. Using default value of 1.")
        start_week = 1

    print(f"Starting processing from Week {start_week}")

    week_files = sorted([f for f in os.listdir('.') if f.startswith('Week_') and f.endswith('.md')])
    for filename in week_files:
        week_number = int(filename.split('_')[1].split('.')[0])
        if week_number >= start_week:
            process_file(filename)
        else:
            print(f"Skipping file: {filename}")

if __name__ == "__main__":
    main()