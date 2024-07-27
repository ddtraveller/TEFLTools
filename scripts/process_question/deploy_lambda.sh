#!/bin/bash
set -ex
# Set variables
FUNCTION_NAME="AnthropicQuestionAnswerer"
ROLE_NAME="AnthropicLambdaRole"
S3_BUCKET="tl-web"
S3_KEY="lambda-deployment-package.zip"
REGION="us-west-2"

# Create deployment package
echo "Creating deployment package..."
zip -r9 ${S3_KEY} lambda_handler.py
pip install anthropic -t .
zip -r9 ${S3_KEY} anthropic

# Upload deployment package to S3
echo "Uploading deployment package to S3..."
aws s3 cp ${S3_KEY} s3://${S3_BUCKET}/${S3_KEY}

# Create IAM role for Lambda
echo "Creating IAM role..."
ROLE_ARN=$(aws iam create-role --role-name ${ROLE_NAME} --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}' --query 'Role.Arn' --output text)

# Attach necessary policies to the role
echo "Attaching policies to role..."
aws iam attach-role-policy --role-name ${ROLE_NAME} --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
aws iam attach-role-policy --role-name ${ROLE_NAME} --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

# Wait for role to be created
echo "Waiting for role to be created..."
sleep 10

# Create Lambda function
echo "Creating Lambda function..."
aws lambda create-function \
    --function-name ${FUNCTION_NAME} \
    --runtime python3.9 \
    --role ${ROLE_ARN} \
    --handler lambda_function.lambda_handler \
    --code S3Bucket=${S3_BUCKET},S3Key=${S3_KEY} \
    --region ${REGION}

# Configure S3 trigger
echo "Configuring S3 trigger..."
aws lambda add-permission \
    --function-name ${FUNCTION_NAME} \
    --statement-id s3-trigger \
    --action lambda:InvokeFunction \
    --principal s3.amazonaws.com \
    --source-arn arn:aws:s3:::${S3_BUCKET}

# Create Lambda function URL
echo "Creating Lambda function URL..."
aws lambda create-function-url-config \
    --function-name ${FUNCTION_NAME} \
    --auth-type NONE \
    --cors '{
        "AllowOrigins": ["*"],
        "AllowMethods": ["*"],
        "AllowHeaders": ["*"],
        "ExposeHeaders": ["*"],
        "MaxAge": 0,
        "AllowCredentials": false
    }'

# Get the created function URL
FUNCTION_URL=$(aws lambda get-function-url-config --function-name ${FUNCTION_NAME} --query 'FunctionUrl' --output text)

echo "Lambda function deployed and configured successfully."
echo "Function URL: ${FUNCTION_URL}"