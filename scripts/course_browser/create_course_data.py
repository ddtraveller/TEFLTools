import boto3
import json

# Create an S3 client
s3 = boto3.client('s3')

# Set the bucket name
bucket_name = 'tl-web'

# Set the prefixes for the folders
prefixes = ['activities/', 'lesson_plans/', 'syllabus/']

# Create a dictionary to store the file paths
course_data = {}

# Iterate over the prefixes
for prefix in prefixes:
    print(f"Files in {prefix}:")
    
    # List objects in the bucket with the specified prefix
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    
    # Extract the file paths and store them in the course_data dictionary
    file_paths = [obj['Key'] for obj in response.get('Contents', [])]
    course_data[prefix.rstrip('/')] = file_paths
    
    print(file_paths)
    print()  # Print a blank line for separation

# Save the course_data dictionary as a JSON file
with open('course_data.json', 'w') as json_file:
    json.dump(course_data, json_file, indent=4)

print("course_data.json created successfully.")