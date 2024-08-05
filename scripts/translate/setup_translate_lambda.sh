#!/bin/bash
set -ex

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
STACK_NAME="EnglishTetumTranslator"
ECR_REPOSITORY_NAME="english-tetum-translator"
REGION="us-west-2"

# Ensure ECR repository exists
aws ecr describe-repositories --repository-names $ECR_REPOSITORY_NAME --region $REGION || \
aws ecr create-repository --repository-name $ECR_REPOSITORY_NAME --region $REGION

# Build Docker image
echo "Building Docker image..."
docker build -t $ECR_REPOSITORY_NAME .

# Get ECR repository URI
ECR_REPOSITORY_URI=$(aws ecr describe-repositories --repository-names $ECR_REPOSITORY_NAME --query 'repositories[0].repositoryUri' --output text)

# Login to ECR
echo "Logging in to ECR..."
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ECR_REPOSITORY_URI

echo "Tagging and pushing image to ECR..."
docker tag english-tetum-translator:latest 874956223356.dkr.ecr.us-west-2.amazonaws.com/english-tetum-translator:latest
docker push 874956223356.dkr.ecr.us-west-2.amazonaws.com/english-tetum-translator:latest

if aws cloudformation describe-stacks --stack-name EnglishTetumTranslator --region us-west-2 &>/dev/null; then
    echo "Stack exists. Attempting to update..."
    if ! aws cloudformation update-stack --stack-name EnglishTetumTranslator \
        --template-body file:///home/ubuntu/environment/TEFLTools/scripts/translate/cloudformation.yaml \
        --parameters ParameterKey=AnthropicApiKey,ParameterValue=${ANTHROPIC_API_KEY} \
        --capabilities CAPABILITY_IAM --region us-west-2 2>&1 | grep -q 'No updates are to be performed'; then
        echo "Waiting for stack update to complete..."
        aws cloudformation wait stack-update-complete --stack-name EnglishTetumTranslator --region us-west-2
    else
        echo "No updates were performed on the CloudFormation stack."
    fi
else
    echo "Stack does not exist. Creating..."
    aws cloudformation create-stack --stack-name EnglishTetumTranslator \
        --template-body file:///home/ubuntu/environment/TEFLTools/scripts/translate/cloudformation.yaml \
        --parameters ParameterKey=AnthropicApiKey,ParameterValue=${ANTHROPIC_API_KEY} \
        --capabilities CAPABILITY_IAM --region us-west-2
    echo "Waiting for stack creation to complete..."
    aws cloudformation wait stack-create-complete --stack-name EnglishTetumTranslator --region us-west-2
fi

# Get Lambda function name
LAMBDA_FUNCTION_NAME=$(aws cloudformation describe-stack-resource --stack-name EnglishTetumTranslator --logical-resource-id TranslationLambdaFunction --query 'StackResourceDetail.PhysicalResourceId' --output text --region us-west-2)

# Update Lambda function
echo "Updating Lambda function..."
aws lambda update-function-code --function-name "$LAMBDA_FUNCTION_NAME" --image-uri 874956223356.dkr.ecr.us-west-2.amazonaws.com/english-tetum-translator:latest --region us-west-2

# Verify update
echo "Verifying Lambda function update..."
aws lambda get-function --function-name "$LAMBDA_FUNCTION_NAME" --query 'Configuration.LastModified' --region us-west-2

echo "Deployment completed successfully."