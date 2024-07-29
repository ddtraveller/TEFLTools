#!/bin/bash
set -ex

# Set variables
STANZA_LAYER_NAME="stanza-layer"
RUNTIME="python3.9"
TEMP_DIR="/tmp/lambda_layers"

# Clean up any existing temporary directory
rm -rf "${TEMP_DIR}"

# Create Stanza layer directory
STANZA_LAYER_DIR="${TEMP_DIR}/${STANZA_LAYER_NAME}"
mkdir -p "${STANZA_LAYER_DIR}/python"

# Install Stanza in the layer directory
pip install stanza==1.4.2 --target "${STANZA_LAYER_DIR}/python" --no-cache-dir

# Download Stanza English model
PYTHONPATH="${STANZA_LAYER_DIR}/python" python -c "
import os
import sys
sys.path.insert(0, '${STANZA_LAYER_DIR}/python')
import stanza
os.environ['STANZA_RESOURCES_DIR'] = '${STANZA_LAYER_DIR}/python/stanza_resources'
stanza.download('en', processors='tokenize,pos,lemma')
"

# Create ZIP file for Stanza layer
cd "${STANZA_LAYER_DIR}"
zip -r "${STANZA_LAYER_NAME}.zip" python

# Get the account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Publish new layer version
STANZA_LAYER_ARN=$(aws lambda publish-layer-version \
    --layer-name "${STANZA_LAYER_NAME}" \
    --description "Layer for Stanza NLP library with English model" \
    --license-info "MIT" \
    --zip-file "fileb://${STANZA_LAYER_NAME}.zip" \
    --compatible-runtimes "${RUNTIME}" \
    --query 'LayerVersionArn' \
    --output text)

echo "Stanza Layer ARN: ${STANZA_LAYER_ARN}"

# Remove the ZIP file to free up space
rm "${STANZA_LAYER_NAME}.zip"

# Clean up
rm -rf "${TEMP_DIR}"

echo "Stanza Lambda layer created successfully."