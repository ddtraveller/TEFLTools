#!/bin/bash
set -e

# Configuration
LAMBDA_FUNCTION_NAME="ContactForm"
LAMBDA_DESCRIPTION="Lambda function for handling contact form submissions"
RUNTIME="python3.9"
HANDLER="lambda_function.lambda_handler"
TIMEOUT=30
MEMORY_SIZE=128
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEMP_DIR="/tmp/${LAMBDA_FUNCTION_NAME}"
ROLE_NAME="${LAMBDA_FUNCTION_NAME}-role"
REGION="us-west-2"
SNS_TOPIC_ARN="arn:aws:sns:us-west-2:874956223356:my_email"

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
        --output text \
        --no-cli-pager)
    
    echo "Attaching AWSLambdaBasicExecutionRole policy"
    aws iam attach-role-policy \
        --role-name "${ROLE_NAME}" \
        --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole \
        --no-cli-pager
    
    echo "Attaching SNS publish policy"
    aws iam put-role-policy \
        --role-name "${ROLE_NAME}" \
        --policy-name SNSPublishPolicy \
        --policy-document '{
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Action": "sns:Publish",
                "Resource": "'"${SNS_TOPIC_ARN}"'"
            }]
        }' \
        --no-cli-pager
    
    echo "Waiting for role to be available..."
    aws iam get-role --role-name "${ROLE_NAME}" --no-cli-pager
    sleep 10  # Wait for role to be fully available
}

# Check if role exists, create if it doesn't
if ! aws iam get-role --role-name "${ROLE_NAME}" --no-cli-pager >/dev/null 2>&1; then
    create_lambda_role
else
    echo "Using existing role: ${ROLE_NAME}"
    ROLE_ARN=$(aws iam get-role --role-name "${ROLE_NAME}" --query 'Role.Arn' --output text --no-cli-pager)
fi
echo "Role ARN: ${ROLE_ARN}"

# Clean up any existing temporary directory
rm -rf "${TEMP_DIR}"
mkdir -p "${TEMP_DIR}"

# Copy Lambda function code
cp "${SCRIPT_DIR}/lambda_function.py" "${TEMP_DIR}/"

# Create a requirements.txt file
cat << EOF > "${TEMP_DIR}/requirements.txt"
boto3==1.28.38
EOF

# Install dependencies
pip install -r "${TEMP_DIR}/requirements.txt" --target "${TEMP_DIR}" --only-binary=:all: --implementation cp --python-version 3.9

# Create a ZIP file with the Lambda function and dependencies
cd "${TEMP_DIR}"
zip -r9 "${LAMBDA_FUNCTION_NAME}.zip" .

# Function to wait for Lambda update
wait_for_lambda_update() {
    echo "Waiting for the Lambda function update to complete..."
    while true; do
        STATUS=$(aws lambda get-function --function-name "${LAMBDA_FUNCTION_NAME}" --query 'Configuration.LastUpdateStatus' --output text --region "${REGION}" --no-cli-pager)
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
if aws lambda get-function --function-name "${LAMBDA_FUNCTION_NAME}" --region "${REGION}" --no-cli-pager >/dev/null 2>&1; then
    echo "Updating existing Lambda function"
    aws lambda update-function-code \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --zip-file "fileb://${LAMBDA_FUNCTION_NAME}.zip" \
        --region "${REGION}" \
        --no-cli-pager
    
    wait_for_lambda_update
    
    aws lambda update-function-configuration \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --runtime "${RUNTIME}" \
        --handler "${HANDLER}" \
        --role "${ROLE_ARN}" \
        --timeout "${TIMEOUT}" \
        --memory-size "${MEMORY_SIZE}" \
        --region "${REGION}" \
        --no-cli-pager
        
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
        --region "${REGION}" \
        --no-cli-pager
    
    wait_for_lambda_update
fi

# Create or update Lambda function URL
if aws lambda get-function-url-config --function-name "${LAMBDA_FUNCTION_NAME}" --region "${REGION}" --no-cli-pager >/dev/null 2>&1; then
    echo "Updating Lambda function URL..."
    FUNCTION_URL=$(aws lambda update-function-url-config \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --auth-type NONE \
        --cors '{
            "AllowOrigins": ["*"],
            "AllowMethods": ["POST"],
            "AllowHeaders": ["content-type"],
            "ExposeHeaders": ["date", "keep-alive"]
        }' \
        --query 'FunctionUrl' \
        --output text \
        --region "${REGION}" \
        --no-cli-pager)
else
    echo "Creating Lambda function URL..."
    FUNCTION_URL=$(aws lambda create-function-url-config \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --auth-type NONE \
        --cors '{
            "AllowOrigins": ["*"],
            "AllowMethods": ["POST"],
            "AllowHeaders": ["content-type"],
            "ExposeHeaders": ["date", "keep-alive"]
        }' \
        --query 'FunctionUrl' \
        --output text \
        --region "${REGION}" \
        --no-cli-pager)

    echo "Adding Lambda function URL permissions..."
    aws lambda add-permission \
        --function-name "${LAMBDA_FUNCTION_NAME}" \
        --statement-id FunctionURLAllowPublicAccess \
        --action lambda:InvokeFunctionUrl \
        --principal "*" \
        --function-url-auth-type NONE \
        --region "${REGION}" \
        --no-cli-pager
fi

# Get the updated Lambda function details
LAMBDA_INFO=$(aws lambda get-function \
    --function-name "${LAMBDA_FUNCTION_NAME}" \
    --region "${REGION}" \
    --no-cli-pager)

# Extract and display the last modified date
LAST_MODIFIED=$(echo "${LAMBDA_INFO}" | jq -r '.Configuration.LastModified')
echo "Lambda function update completed. Last modified: ${LAST_MODIFIED}"

# Clean up
cd -
rm -rf "${TEMP_DIR}"
echo "Lambda function ${LAMBDA_FUNCTION_NAME} created/updated successfully."
echo "Lambda Function URL: ${FUNCTION_URL}"