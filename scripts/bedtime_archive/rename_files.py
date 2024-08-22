import boto3
import re
from urllib.parse import unquote

def clean_title(title):
    # Remove any non-alphanumeric characters and replace spaces with underscores
    clean = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    words = clean.lower().split()
    # Limit to 3 words
    return '_'.join(words[:3])

def rename_files():
    s3 = boto3.client('s3')
    bucket_name = 'tl-web'
    prefix = 'stories/bedtime_'

    # List all objects with the given prefix
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    for obj in response.get('Contents', []):
        old_key = obj['Key']
        if old_key.endswith('.html'):
            # Extract the timestamp
            timestamp = old_key.split('_')[-1].split('.')[0]
            
            # Get the object to read its content
            file_obj = s3.get_object(Bucket=bucket_name, Key=old_key)
            content = file_obj['Body'].read().decode('utf-8')
            
            # Extract title from content (assuming it's in a <title> tag)
            title_match = re.search(r'<title>(.*?)</title>', content)
            if title_match:
                title = title_match.group(1)
                clean_title_part = clean_title(title)
                
                # Construct new key
                new_key = f'stories/bedtime_{clean_title_part}_{timestamp}.html'
                
                # Copy object to new key
                s3.copy_object(Bucket=bucket_name, CopySource={'Bucket': bucket_name, 'Key': old_key}, Key=new_key)
                
                # Delete old object
                s3.delete_object(Bucket=bucket_name, Key=old_key)
                
                print(f"Renamed {old_key} to {new_key}")
            else:
                print(f"Could not find title in {old_key}")

if __name__ == "__main__":
    rename_files()