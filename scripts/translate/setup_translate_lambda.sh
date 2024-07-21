#!/bin/bash
set -e
set -x

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LAMBDA_FILE="lambda_function.py"
STACK_NAME="EnglishTetumTranslator"
S3_BUCKET="tl-web"
LAMBDA_S3_KEY="function.zip"

# Create a temporary directory
TEMP_DIR=$(mktemp -d)
echo "Created temporary directory: $TEMP_DIR"

# Copy Lambda function to temporary directory
cp "$SCRIPT_DIR/$LAMBDA_FILE" "$TEMP_DIR/"

# Create a ZIP file
cd "$TEMP_DIR"
zip -r9 "$SCRIPT_DIR/function.zip" .
cd "$SCRIPT_DIR"

# Upload the new ZIP file to S3
echo "Uploading Lambda function package to S3..."
aws s3 cp "function.zip" "s3://$S3_BUCKET/$LAMBDA_S3_KEY"
aws s3 cp template.html s3://tl-web/template.html

# Update Lambda function code
echo "Updating Lambda function code..."
LAMBDA_FUNCTION_NAME=$(aws cloudformation describe-stack-resource --stack-name "$STACK_NAME" --logical-resource-id TranslationLambdaFunction --query 'StackResourceDetail.PhysicalResourceId' --output text)
aws lambda update-function-code --function-name "$LAMBDA_FUNCTION_NAME" --s3-bucket "$S3_BUCKET" --s3-key "$LAMBDA_S3_KEY"

# Clean up
rm -rf "$TEMP_DIR" "function.zip"

echo "Lambda function updated successfully."