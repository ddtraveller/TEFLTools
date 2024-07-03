import boto3
from urllib.parse import quote
import os

# Configuration
BUCKET_NAME = "tl-tefl"
TEMPLATE_FILE = "template.html"
OUTPUT_FILE = "index.html"

def generate_html_content(files):
    content = ""
    for file in files:
        if file.endswith('/'):
            # It's a folder, don't make it a link
            content += f"        <li>{file}</li>\n"
        else:
            # It's a file, create a link
            encoded_file = quote(file)
            content += f'        <li><a href="https://{BUCKET_NAME}.s3.amazonaws.com/{encoded_file}">{file}</a></li>\n'
    return content

def main():
    # Initialize S3 client
    s3 = boto3.client('s3')

    print(f"Fetching file list from {BUCKET_NAME}...")
    
    # Get the list of files from the S3 bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
    if 'Contents' not in response:
        print("No files found in the bucket or error occurred while fetching file list.")
        return

    files = [obj['Key'] for obj in response['Contents']]
    
    # Print the file list for debugging
    print("Files found in the bucket:")
    for file in files:
        print(f"* {file}")

    # Generate the HTML content
    print("Generating HTML content...")
    content = generate_html_content(files)

    # Check if content is empty
    if not content:
        print("No content generated. Check if there are any files in the bucket.")
        return

    # Read the template file
    try:
        with open(TEMPLATE_FILE, 'r') as file:
            template = file.read()
    except FileNotFoundError:
        print(f"Template file {TEMPLATE_FILE} not found.")
        return

    # Replace the placeholder with the generated content
    output = template.replace("<!-- FILE_LIST_PLACEHOLDER -->", content)

    # Write the output file
    with open(OUTPUT_FILE, 'w') as file:
        file.write(output)

    # Check if the output file was created and has content
    if not os.path.getsize(OUTPUT_FILE):
        print("Output file is empty. Check if the placeholder exists in the template and if content was generated.")
        return

    print(f"Contents of {OUTPUT_FILE}:")
    with open(OUTPUT_FILE, 'r') as file:
        print(file.read())

    # Upload the generated HTML file to S3
    print(f"Uploading {OUTPUT_FILE} to s3://{BUCKET_NAME}/")
    s3.upload_file(OUTPUT_FILE, BUCKET_NAME, OUTPUT_FILE, ExtraArgs={'ContentType': "text/html"})

    print("Process completed. Please check the S3 bucket for the updated index.html.")

if __name__ == "__main__":
    main()