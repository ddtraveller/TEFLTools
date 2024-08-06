#!/bin/bash
set -ex  # Exit on error and print commands

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Configuration
FUNCTION_NAME="exam-builder-lambda"
ROLE_NAME="exam-builder-lambda-role"
FUNCTION_HANDLER="app.lambda_handler"
RUNTIME="python3.9"
TIMEOUT=30
MEMORY_SIZE=256

# Create a temporary directory for packaging
TEMP_DIR=$(mktemp -d)

# Install dependencies into the temporary directory
pip install -r "$SCRIPT_DIR/requirements.txt" -t "$TEMP_DIR"

# Copy your Lambda function code and HTML template to the temporary directory
cp "$SCRIPT_DIR/app.py" "$SCRIPT_DIR/template.html" "$SCRIPT_DIR/take_exam.html" "$TEMP_DIR"

# Create deployment package
echo "Creating deployment package..."
(cd "$TEMP_DIR" && zip -r "$SCRIPT_DIR/deployment_package.zip" .)

# Verify the deployment package exists
if [ ! -f "$SCRIPT_DIR/deployment_package.zip" ]; then
    echo "Error: deployment_package.zip not created"
    exit 1
fi

# Create or update IAM role
echo "Creating/updating IAM role..."
ROLE_ARN=$(aws iam get-role --role-name $ROLE_NAME --query 'Role.Arn' --output text 2>&1)
if echo "$ROLE_ARN" | grep -q "NoSuchEntity"; then
    echo "IAM role does not exist. Creating new IAM role..."
    ROLE_ARN=$(aws iam create-role --role-name $ROLE_NAME \
        --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{"Effect": "Allow","Principal": {"Service": "lambda.amazonaws.com"},"Action": "sts:AssumeRole"}]}' \
        --query 'Role.Arn' --output text)
    
    echo "IAM role created successfully. ARN: $ROLE_ARN"
    
    # Attach necessary policies
    echo "Attaching policies to the role..."
    aws iam attach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
    aws iam attach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
    
    # Wait for role to propagate
    echo "Waiting for role to propagate..."
    sleep 10
elif ! echo "$ROLE_ARN" | grep -q "arn:aws:iam::"; then
    echo "Unexpected response when checking for IAM role:"
    echo "$ROLE_ARN"
    exit 1
else
    echo "IAM role already exists. ARN: $ROLE_ARN"
fi

wait_for_lambda_update() {
    echo "Waiting for Lambda function update to complete..."
    while true; do
        STATUS=$(aws lambda get-function --function-name $FUNCTION_NAME --query 'Configuration.LastUpdateStatus' --output text)
        if [ "$STATUS" = "Successful" ]; then
            echo "Update completed successfully."
            break
        elif [ "$STATUS" = "Failed" ]; then
            echo "Update failed. Check the Lambda function logs for more information."
            exit 1
        fi
        echo "Status: $STATUS. Waiting..."
        sleep 5
    done
}

# Create or update Lambda function
echo "Creating/updating Lambda function..."
if ! FUNCTION_ARN=$(aws lambda get-function --function-name $FUNCTION_NAME --query 'Configuration.FunctionArn' --output text 2>/dev/null); then
    echo "Creating new Lambda function..."
    FUNCTION_ARN=$(aws lambda create-function --function-name $FUNCTION_NAME \
        --zip-file fileb://"$SCRIPT_DIR/deployment_package.zip" \
        --handler $FUNCTION_HANDLER --runtime $RUNTIME \
        --role $ROLE_ARN --timeout $TIMEOUT --memory-size $MEMORY_SIZE \
        --query 'FunctionArn' --output text)
else
    echo "Updating existing Lambda function code..."
    aws lambda update-function-code --function-name $FUNCTION_NAME \
        --zip-file fileb://"$SCRIPT_DIR/deployment_package.zip"
    
    wait_for_lambda_update

    echo "Updating Lambda function configuration..."
    aws lambda update-function-configuration --function-name $FUNCTION_NAME \
        --handler $FUNCTION_HANDLER --runtime $RUNTIME \
        --role $ROLE_ARN --timeout $TIMEOUT --memory-size $MEMORY_SIZE
    
    wait_for_lambda_update
fi

FUNCTION_URL=$(echo $URL_CONFIG | jq -r '.FunctionUrl')

echo "Deployment complete!"
echo "Function ARN: $FUNCTION_ARN"
echo "Function URL: $FUNCTION_URL"

# Clean up
rm "$SCRIPT_DIR/deployment_package.zip"
rm -rf "$TEMP_DIR"