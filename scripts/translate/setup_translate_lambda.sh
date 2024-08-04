#!/bin/bash
set -ex
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LAMBDA_FILE="lambda_function.py"
REQUIREMENTS_FILE="requirements.txt"
STACK_NAME="EnglishTetumTranslator"

# Create a temporary directory
TEMP_DIR=$(mktemp -d)
echo "Created temporary directory: $TEMP_DIR"

# Copy Lambda function, requirements, JSON files, and template.html to temporary directory
cp "$SCRIPT_DIR/$LAMBDA_FILE" "$TEMP_DIR/"
cp "$SCRIPT_DIR/$REQUIREMENTS_FILE" "$TEMP_DIR/"
cp "$SCRIPT_DIR/dictionary.json" "$TEMP_DIR/"
cp "$SCRIPT_DIR/phrases.json" "$TEMP_DIR/"
cp "$SCRIPT_DIR/compound.json" "$TEMP_DIR/"
cp "$SCRIPT_DIR/E2T.txt" "$TEMP_DIR/"
cp "$SCRIPT_DIR/T2E.txt" "$TEMP_DIR/"
cp "$SCRIPT_DIR/template.html" "$TEMP_DIR/"

# Install dependencies for Lambda
echo "Installing dependencies..."
pip install -r $TEMP_DIR/requirements.txt --platform manylinux2014_x86_64 --target $TEMP_DIR --only-binary=:all: --implementation cp --python-version 3.9 || { echo "Failed to install dependencies"; exit 1; }

# Create a ZIP file
cd "$TEMP_DIR"
zip -r9 "$SCRIPT_DIR/function.zip" . || { echo "Failed to create zip file"; exit 1; }
cd "$SCRIPT_DIR"

# Retrieve the Lambda function name
LAMBDA_FUNCTION_NAME=$(aws cloudformation describe-stack-resource --stack-name "$STACK_NAME" --logical-resource-id TranslationLambdaFunction --query 'StackResourceDetail.PhysicalResourceId' --output text)

# Update Lambda function code
echo "Updating Lambda function code..."
aws lambda update-function-code --function-name "$LAMBDA_FUNCTION_NAME" --zip-file "fileb://function.zip" || { echo "Failed to update Lambda function"; exit 1; }

# Verify update
echo "Verifying Lambda function update..."
aws lambda get-function --function-name "$LAMBDA_FUNCTION_NAME" --query 'Configuration.LastModified'

# Clean up
rm -rf "$TEMP_DIR" "function.zip"
echo "Lambda function updated successfully."