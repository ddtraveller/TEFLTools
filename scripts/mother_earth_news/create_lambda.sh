#!/bin/bash
set -ex

# Set variables
LAMBDA_FUNCTION_NAME="mother-earth-news-lambda"
LAMBDA_DESCRIPTION="Lambda function for Mother Earth News analysis"
RUNTIME="python3.9"
HANDLER="lambda_function.lambda_handler"
TIMEOUT=300
MEMORY_SIZE=512
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEMP_DIR="/tmp/${LAMBDA_FUNCTION_NAME}"
ROLE_NAME="${LAMBDA_FUNCTION_NAME}-role"

# Function to create IAM role
create_lambda_role() {
    echo "Creating IAM role: ${ROLE_NAME}"
    ROLE_ARN=$(aws iam create-role \
        --role-name "${ROLE_NAME}" \
        --assume-role-policy-document '{
            "Version": "2012-10-17",
            "Statement": [{
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                }
            }]
        }' \
        --query 'Role.Arn' \
        --output text)
    
    echo "Attaching AWSLambdaBasicExecutionRole policy"
    aws iam attach-role-policy \
        --role-name "${ROLE_NAME}" \
        --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
    
    echo "Waiting for role to be available..."
    aws iam get-role --role-name "${ROLE_NAME}"
    sleep 10  # Wait for role to be fully available
}

# Check if role exists, create if it doesn't
if ! aws iam get-role --role-name "${ROLE_NAME}" >/dev/null 2>&1; then
    create_lambda_role
else
    echo "Using existing role: ${ROLE_NAME}"
    ROLE_ARN=$(aws iam get-role --role-name "${ROLE_NAME}" --query 'Role.Arn' --output text)
fi

echo "Role ARN: ${ROLE_ARN}"

# Clean up any existing temporary directory
rm -rf "${TEMP_DIR}"
mkdir -p "${TEMP_DIR}"

# Copy Lambda function code and .js files
cp "${SCRIPT_DIR}/lambda_function.py" "${TEMP_DIR}/"
cp "${SCRIPT_DIR}"/*.js "${TEMP_DIR}/"

# Create a virtual environment and install dependencies
python3 -m venv "${TEMP_DIR}/venv"
source "${TEMP_DIR}/venv/bin/activate"
pip install --upgrade pip
pip install \
    anthropic==0.2.8 \
    tiktoken==0.3.3 \
    boto3==1.28.38 \
    requests==2.31.0 \
    tokenizers==0.13.2 \    
    -t "${TEMP_DIR}"

# Deactivate and remove virtual environment
deactivate
rm -rf "${TEMP_DIR}/venv"

# Create a ZIP file with the Lambda function, .js files, and dependencies
cd "${TEMP_DIR}"
zip -r "${LAMBDA_FUNCTION_NAME}.zip" .

# Create or update the Lambda function
if aws lambda get-function --function-name "${LAMBDA_FUNCTION_NAME}" >/dev/null 2>&1; then
    echo "Updating existing Lambda function"
    aws lambda update-function-code \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --zip-file "fileb://${LAMBDA_FUNCTION_NAME}.zip"
    
    aws lambda update-function-configuration \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --runtime "${RUNTIME}" \
        --handler "${HANDLER}" \
        --role "${ROLE_ARN}" \
        --timeout "${TIMEOUT}" \
        --memory-size "${MEMORY_SIZE}"
else
    echo "Creating new Lambda function"
    aws lambda create-function \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --runtime "${RUNTIME}" \
        --handler "${HANDLER}" \
        --role "${ROLE_ARN}" \
        --zip-file "fileb://${LAMBDA_FUNCTION_NAME}.zip" \
        --description "${LAMBDA_DESCRIPTION}" \
        --timeout "${TIMEOUT}" \
        --memory-size "${MEMORY_SIZE}"
fi

# Clean up
rm -rf "${TEMP_DIR}"

echo "Lambda function ${LAMBDA_FUNCTION_NAME} created/updated successfully."