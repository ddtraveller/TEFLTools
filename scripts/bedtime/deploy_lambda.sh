#!/bin/bash
set -e

# Set variables
LAMBDA_FUNCTION_NAME="bedtime-story-lambda"
LAMBDA_DESCRIPTION="Lambda function for generating bedtime stories"
RUNTIME="python3.9"
HANDLER="lambda_function.lambda_handler"
TIMEOUT=300
MEMORY_SIZE=512
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEMP_DIR="/tmp/${LAMBDA_FUNCTION_NAME}"
ROLE_NAME="${LAMBDA_FUNCTION_NAME}-role"
BUCKET_NAME="tl-web"
REGION="us-west-2"  # Replace with your AWS region if different

# Check for API keys in environment variables, prompt if not found
if [ -z "$ANTHROPIC_API_KEY" ]; then
    read -p "Enter your Anthropic API key: " ANTHROPIC_API_KEY
fi

if [ -z "$STABILITY_API_KEY" ]; then
    read -p "Enter your Stability AI API key: " STABILITY_API_KEY
fi

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
cp "${SCRIPT_DIR}"/*.json "${TEMP_DIR}/"

# Create a requirements.txt file
cat << EOF > "${TEMP_DIR}/requirements.txt"
anthropic==0.5.0
tiktoken==0.3.3
boto3==1.28.38
requests==2.31.0
EOF

# Install dependencies
pip install -r "${TEMP_DIR}/requirements.txt" --target "${TEMP_DIR}" --only-binary=:all: --implementation cp --python-version 3.9

# Create a ZIP file with the Lambda function, .js files, and dependencies
cd "${TEMP_DIR}"
zip -r9 "${LAMBDA_FUNCTION_NAME}.zip" .

# Function to wait for Lambda update
wait_for_lambda_update() {
    echo "Waiting for the Lambda function update to complete..."
    while true; do
        STATUS=$(aws lambda get-function --function-name "${LAMBDA_FUNCTION_NAME}" --query 'Configuration.LastUpdateStatus' --output text --region "${REGION}")
        if [ "$STATUS" = "Successful" ]; then
            echo "Update completed successfully."
            break
        elif [ "$STATUS" = "Failed" ]; then
            echo "Update failed. Please check the Lambda function logs."
            exit 1
        fi
        echo "Current status: $STATUS. Waiting..."
        sleep 5
    done
}

# Create or update the Lambda function
if aws lambda get-function --function-name "${LAMBDA_FUNCTION_NAME}" --region "${REGION}" >/dev/null 2>&1; then
    echo "Updating existing Lambda function"
    aws lambda update-function-code \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --zip-file "fileb://${LAMBDA_FUNCTION_NAME}.zip" \
        --region "${REGION}"
    
    wait_for_lambda_update
    
    aws lambda update-function-configuration \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --runtime "${RUNTIME}" \
        --handler "${HANDLER}" \
        --role "${ROLE_ARN}" \
        --timeout "${TIMEOUT}" \
        --memory-size "${MEMORY_SIZE}" \
        --environment "Variables={ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY},STABILITY_API_KEY=${STABILITY_API_KEY}}" \
        --region "${REGION}"
    
    wait_for_lambda_update
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
        --memory-size "${MEMORY_SIZE}" \
        --environment "Variables={ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY},STABILITY_API_KEY=${STABILITY_API_KEY}}" \
        --region "${REGION}"
    
    wait_for_lambda_update
fi

# Get the updated Lambda function details
LAMBDA_INFO=$(aws lambda get-function \
    --function-name "${LAMBDA_FUNCTION_NAME}" \
    --region "${REGION}")

# Extract and display the last modified date
LAST_MODIFIED=$(echo "${LAMBDA_INFO}" | jq -r '.Configuration.LastModified')
echo "Lambda function update completed. Last modified: ${LAST_MODIFIED}"

# Clean up
cd -
rm -rf "${TEMP_DIR}"
echo "Lambda function ${LAMBDA_FUNCTION_NAME} created/updated successfully."