import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Set the bucket name
bucket_name = 'tl-web'

# Set the prefixes for the folders
prefixes = ['activities/', 'lesson-plans/', 'syllabus/']

# Iterate over the prefixes
for prefix in prefixes:
    print(f"Files in {prefix}:")
    
    # List objects in the bucket with the specified prefix
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    
    # Iterate over the objects
    for obj in response.get('Contents', []):
        print(obj['Key'])
    
    print()  # Print a blank line for separation