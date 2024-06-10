#!/bin/bash
set -ex

# Function name
FUNCTION_NAME="timor-leste-map-updater"

# IAM role name
ROLE_NAME="lambda-execution-role"

# Create IAM role for Lambda function if it doesn't exist
if ! aws iam get-role --role-name $ROLE_NAME >/dev/null 2>&1; then
  aws iam create-role --role-name $ROLE_NAME \
    --assume-role-policy-document '{
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
    }'
else
  echo "IAM role $ROLE_NAME already exists"
fi

# Attach necessary permissions to the IAM role
aws iam attach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Get the IAM role ARN
ROLE_ARN=$(aws iam get-role --role-name $ROLE_NAME --query 'Role.Arn' --output text)

# Create a temporary directory
mkdir -p package
pip install --target ./package folium boto3 numpy jinja2 branca requests
cd package
zip -r ../deployment_package.zip .

cd ..
zip deployment_package.zip lambda_function.py

rm -rf package

# Check if the Lambda function exists
if aws lambda get-function --function-name $FUNCTION_NAME >/dev/null 2>&1; then
  # Update the Lambda function code
  aws lambda update-function-code --function-name $FUNCTION_NAME --zip-file fileb://deployment_package.zip
else
  # Create the Lambda function
  aws lambda create-function --function-name $FUNCTION_NAME \
    --runtime python3.8 \
    --role $ROLE_ARN \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://deployment_package.zip
fi

# Clean up the deployment package
rm deployment_package.zip