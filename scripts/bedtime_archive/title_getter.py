import boto3
import re
from bs4 import BeautifulSoup
import tempfile
import os

def get_html_title(content):
    soup = BeautifulSoup(content, 'html.parser')
    title_tag = soup.find('title')
    return title_tag.string if title_tag else None

def generate_html_links():
    s3 = boto3.client('s3')
    bucket_name = 'tl-web'
    prefix = 'stories/'

    html_links = []

    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        for obj in page.get('Contents', []):
            if obj['Key'].startswith(prefix + 'bedtime_') and obj['Key'].endswith('.html'):
                response = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
                content = response['Body'].read().decode('utf-8')
                
                title = get_html_title(content)
                if title:
                    url = f"https://{bucket_name}.s3.amazonaws.com/{obj['Key']}"
                    html_links.append(f'<p><a href="{url}">{title}</a></p>')

    return '\n'.join(html_links)

def save_links_to_file(links_html):
    file_path = 'archive_links_temp.html'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('<html>\n<body>\n')
        f.write(links_html)
        f.write('\n</body>\n</html>')
    
    return file_path

if __name__ == "__main__":
    links_html = generate_html_links()
    file_path = save_links_to_file(links_html)
    print(f"Links have been saved to: {file_path}")