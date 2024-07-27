#!/bin/bash
set -ex

# Set variables
FUNCTION_NAME="AnthropicQuestionAnswerer"
S3_BUCKET="tl-web"
S3_KEY="lambda-deployment-package.zip"
REGION="us-west-2"
TEMP_DIR="/tmp/lambda_package"

# Clean up any existing temporary directory
rm -rf $TEMP_DIR
mkdir -p $TEMP_DIR

# Create a requirements.txt file
cat << EOF > $TEMP_DIR/requirements.txt
anthropic
tiktoken
requests
EOF

# Install dependencies for Lambda
pip install -r $TEMP_DIR/requirements.txt --platform manylinux2014_x86_64 --target $TEMP_DIR --only-binary=:all: --implementation cp --python-version 3.9

# Copy the Lambda function code
cp lambda_function.py ${TEMP_DIR}/

# Create zip file
cd ${TEMP_DIR}
zip -r9 ${S3_KEY} .
cd -

# Upload deployment package to S3
echo "Uploading deployment package to S3..."
aws s3 cp ${TEMP_DIR}/${S3_KEY} s3://${S3_BUCKET}/${S3_KEY}

# Update Lambda function code
echo "Updating Lambda function..."
aws lambda update-function-code \
    --function-name ${FUNCTION_NAME} \
    --s3-bucket ${S3_BUCKET} \
    --s3-key ${S3_KEY} \
    --region ${REGION}

# Wait for the update to complete
echo "Waiting for function update to complete..."
aws lambda wait function-updated \
    --function-name ${FUNCTION_NAME} \
    --region ${REGION}

# Clean up
echo "Cleaning up..."
rm -rf ${TEMP_DIR}

echo "Lambda function updated successfully."

# Get the function URL
FUNCTION_URL=$(aws lambda get-function-url-config --function-name ${FUNCTION_NAME} --query 'FunctionUrl' --output text)
echo "Function URL: ${FUNCTION_URL}"