#!/bin/bash
set -ex
# aws s3 ls s3://tl-web/ --recursive --exclude "*" --include "activities/*" --include "lesson-plans/*" --include "syllabus/*"
# Set the S3 bucket name
S3_BUCKET="tl-web"

# Set the folders to be copied
FOLDERS=("../../activities" "../../lesson_plans" "../../syllabus")

# Check if the dry run flag is set
DRY_RUN_FLAG=""
if [ "$1" == "--dry-run" ]; then
  DRY_RUN_FLAG="--dryrun"
fi

# Loop through the folders
for folder in "${FOLDERS[@]}"
do
  # Check if the folder exists in the Git repository
  if [ -d "$folder" ]; then
    # Get the folder name without the path
    folder_name=$(basename "$folder")
    
    # Copy the folder to the S3 bucket, creating the corresponding folder in S3
    aws s3 sync "$folder" "s3://$S3_BUCKET/$folder_name" --delete $DRY_RUN_FLAG
    
    if [ -z "$DRY_RUN_FLAG" ]; then
      echo "Copied $folder_name to S3 bucket $S3_BUCKET"
    else
      echo "Dry run: Copying $folder_name to S3 bucket $S3_BUCKET"
    fi
  else
    echo "Folder $folder not found in the Git repository"
  fi
done