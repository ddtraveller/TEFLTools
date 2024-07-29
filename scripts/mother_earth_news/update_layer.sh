#!/bin/bash
set -ex

# Get the ARN of the latest version of the NLP layer
NLP_LAYER_ARN=$(aws lambda list-layer-versions --layer-name nlp-layer --query 'LayerVersions[0].LayerVersionArn' --output text)

# Get the ARN of the latest version of the main application layer
MAIN_LAYER_ARN=$(aws lambda list-layer-versions --layer-name anthropic-llm-mother-earth-news --query 'LayerVersions[0].LayerVersionArn' --output text)

# Update the Lambda function to use both new layers
aws lambda update-function-configuration \
    --function-name mother-earth-news-lambda \
    --layers $NLP_LAYER_ARN $MAIN_LAYER_ARN

echo "Updated Lambda function with layers:"
echo "NLP Layer: $NLP_LAYER_ARN"
echo "Main Layer: $MAIN_LAYER_ARN"