#!/bin/bash

# Set variables
LAMBDA_FUNCTION_NAME="tl-info-lambda"
TEMP_DIR=$(mktemp -d)
ZIP_FILE="$TEMP_DIR/lambda_function.zip"

# Create a virtual environment
python3 -m venv $TEMP_DIR/venv
source $TEMP_DIR/venv/bin/activate

# Install required packages with specific versions
pip install requests==2.31.0 google-auth==2.22.0 google-auth-oauthlib==1.0.0 boto3==1.28.38 urllib3==1.26.15

# Copy the Lambda function code and rename it to index.py
cp lambda_handler.py $TEMP_DIR/index.py

# Create a directory for the packages
mkdir -p $TEMP_DIR/package

# Install packages to the package directory
pip install -t $TEMP_DIR/package requests==2.31.0 google-auth==2.22.0 google-auth-oauthlib==1.0.0 boto3==1.28.38 urllib3==1.26.15

# Create a ZIP file with the Lambda function and its dependencies
cd $TEMP_DIR/package
zip -r9 $ZIP_FILE .
cd $TEMP_DIR
zip -g $ZIP_FILE index.py

# Update the Lambda function
aws lambda update-function-code --function-name $LAMBDA_FUNCTION_NAME --zip-file fileb://$ZIP_FILE

# Clean up
rm -rf $TEMP_DIR
deactivate

echo "Lambda function updated successfully!"