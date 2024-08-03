import boto3
from botocore.exceptions import ClientError

def get_s3_object_urls(bucket_name, prefix):
    s3 = boto3.client('s3')
    urls = []

    try:
        paginator = s3.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

        for page in pages:
            if 'Contents' in page:
                for obj in page['Contents']:
                    object_key = obj['Key']
                    url = f"https://{bucket_name}.s3.amazonaws.com/{object_key}"
                    urls.append(url)

    except ClientError as e:
        print(f"An error occurred: {e}")
        return None

    return urls

# Usage
bucket_name = 'tl-web'
prefix = 'images/'

urls = get_s3_object_urls(bucket_name, prefix)

if urls:
    for url in urls:
        print(url)
else:
    print("Failed to retrieve URLs or no objects found.")