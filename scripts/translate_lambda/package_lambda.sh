#!/bin/bash
set -ex
# Set variables
BUCKET_NAME="tl-web"
LAMBDA_NAME="EnglishToTetumTranslator"
ZIP_FILE_NAME="${LAMBDA_NAME}.zip"
TEMP_DIR="/tmp/lambda_package"
REGION="us-west-2"  # Replace with your AWS region if different
# Create a temporary directory
rm -rf $TEMP_DIR
mkdir -p $TEMP_DIR
#pydantic==1.10.12
# Create a requirements.txt file
cat << EOF > $TEMP_DIR/requirements.txt
anthropic
tiktoken
EOF
# Install dependencies for Lambda
pip install -r $TEMP_DIR/requirements.txt --platform manylinux2014_x86_64 --target $TEMP_DIR --only-binary=:all: --implementation cp --python-version 3.9
# List all installed packages
pip list --path $TEMP_DIR
# Copy Lambda function code to the temporary directory
cp lambda_function.py $TEMP_DIR/
# Copy JS files to the temporary directory
cp dictionary.json phrases.json compound.json $TEMP_DIR/
# Create a ZIP file
cd $TEMP_DIR
zip -r9 $ZIP_FILE_NAME .
# List contents of the ZIP file
unzip -l $ZIP_FILE_NAME
# Upload the ZIP file to S3
aws s3 cp $ZIP_FILE_NAME s3://$BUCKET_NAME/$ZIP_FILE_NAME
# Update the Lambda function code
aws lambda update-function-code \
    --function-name $LAMBDA_NAME \
    --s3-bucket $BUCKET_NAME \
    --s3-key $ZIP_FILE_NAME \
    --region $REGION
# Update Lambda configuration
aws lambda update-function-configuration \
    --function-name $LAMBDA_NAME \
    --timeout 60 \
    --memory-size 1024 \
    --region $REGION
# Clean up
cd -
rm -rf $TEMP_DIR
echo "Lambda package uploaded to s3://$BUCKET_NAME/$ZIP_FILE_NAME"
echo "Lambda function $LAMBDA_NAME updated with new code"
# Wait for the update to complete
echo "Waiting for the Lambda function update to complete..."
aws lambda wait function-updated \
    --function-name $LAMBDA_NAME \
    --region $REGION
# Get the updated Lambda function details
LAMBDA_INFO=$(aws lambda get-function \
    --function-name $LAMBDA_NAME \
    --region $REGION)
# Extract and display the last modified date
LAST_MODIFIED=$(echo $LAMBDA_INFO | jq -r '.Configuration.LastModified')
echo "Lambda function update completed. Last modified: $LAST_MODIFIED"