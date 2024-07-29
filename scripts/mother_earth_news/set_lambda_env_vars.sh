#!/bin/bash
set -ex

LAMBDA_FUNCTION_NAME="mother-earth-news-lambda"

# Function to prompt for a value
prompt_for_value() {
    local var_name=$1
    local prompt_text=$2
    local default_value=$3
    
    if [ -n "$default_value" ]; then
        read -p "${prompt_text} (current: ${default_value}): " value
        value=${value:-$default_value}
    else
        read -p "${prompt_text}: " value
    fi
    
    echo $value
}

# Get current environment variables
current_env=$(aws lambda get-function-configuration --function-name $LAMBDA_FUNCTION_NAME --query 'Environment.Variables' --output json)

# Extract current values (if they exist)
current_google_api_key=$(echo $current_env | jq -r '.GOOGLE_API_KEY // empty')
current_search_engine_id=$(echo $current_env | jq -r '.SEARCH_ENGINE_ID // empty')
current_anthropic_api_key=$(echo $current_env | jq -r '.ANTHROPIC_API_KEY // empty')
current_s3_bucket=$(echo $current_env | jq -r '.S3_BUCKET // empty')

# Prompt for values
GOOGLE_API_KEY=$(prompt_for_value "GOOGLE_API_KEY" "Enter Google API Key" "$current_google_api_key")
SEARCH_ENGINE_ID=$(prompt_for_value "SEARCH_ENGINE_ID" "Enter Search Engine ID" "$current_search_engine_id")
ANTHROPIC_API_KEY=$(prompt_for_value "ANTHROPIC_API_KEY" "Enter Anthropic API Key" "$current_anthropic_api_key")
S3_BUCKET=$(prompt_for_value "S3_BUCKET" "Enter S3 Bucket Name" "$current_s3_bucket")

# Construct environment variables JSON
env_vars=$(cat <<EOF
{
  "Variables": {
    "GOOGLE_API_KEY": "$GOOGLE_API_KEY",
    "SEARCH_ENGINE_ID": "$SEARCH_ENGINE_ID",
    "ANTHROPIC_API_KEY": "$ANTHROPIC_API_KEY",
    "S3_BUCKET": "$S3_BUCKET"
  }
}
EOF
)

# Update Lambda function configuration
echo "Updating Lambda function environment variables..."
aws lambda update-function-configuration \
    --function-name $LAMBDA_FUNCTION_NAME \
    --environment "$env_vars"

echo "Environment variables updated successfully for $LAMBDA_FUNCTION_NAME"