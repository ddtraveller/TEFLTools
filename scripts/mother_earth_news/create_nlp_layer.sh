#!/bin/bash
set -ex

# Set variables
NLP_LAYER_NAME="nlp-layer-minimal"
RUNTIME="python3.9"
TEMP_DIR="/tmp/lambda_layers"
PYTHON_VERSION="3"

# Clean up any existing temporary directory
rm -rf "${TEMP_DIR}"

# Create a virtual environment and activate it
python${PYTHON_VERSION} -m venv "${TEMP_DIR}/venv"
source "${TEMP_DIR}/venv/bin/activate"

# Upgrade pip and install wheel
pip install --upgrade pip wheel

# Create NLP layer
NLP_LAYER_DIR="${TEMP_DIR}/${NLP_LAYER_NAME}"
mkdir -p "${NLP_LAYER_DIR}/python"
mkdir -p "${NLP_LAYER_DIR}/nltk_data/tokenizers/punkt"

# Install NLTK and tokenizers in the virtual environment
pip install nltk==3.8.1 tokenizers==0.13.2

# Download only English NLTK punkt data
python -m nltk.downloader -d "${NLP_LAYER_DIR}/nltk_data" punkt

# Keep only English punkt data
find "${NLP_LAYER_DIR}/nltk_data/tokenizers/punkt" -type f ! -name "english.pickle" -delete

# Copy the installed packages to the layer directory
pip install nltk==3.8.1 tokenizers==0.13.2 --target "${NLP_LAYER_DIR}/python" --no-cache-dir

# Create ZIP file for NLP layer
cd "${NLP_LAYER_DIR}"
zip -r "${NLP_LAYER_NAME}.zip" python nltk_data

# Get the account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Create new layer
# Publish new layer version and get ARN
NLP_LAYER_ARN=$(aws lambda publish-layer-version \
    --layer-name "${NLP_LAYER_NAME}" \
    --description "Minimal layer for NLP tools including NLTK and tokenizers" \
    --license-info "MIT" \
    --zip-file "fileb://${NLP_LAYER_NAME}.zip" \
    --compatible-runtimes "${RUNTIME}" \
    --query 'LayerVersionArn' \
    --output text)

echo "NLP Layer ARN: ${NLP_LAYER_ARN}"

# Get the latest layer version
LATEST_VERSION=$(aws lambda list-layer-versions --layer-name "${NLP_LAYER_NAME}" --query 'LayerVersions[0].Version' --output text)

# Construct and output the layer ARN
NLP_LAYER_ARN="arn:aws:lambda:$(aws configure get region):${ACCOUNT_ID}:layer:${NLP_LAYER_NAME}:${LATEST_VERSION}"
echo "NLP Layer ARN: ${NLP_LAYER_ARN}"

# Remove the ZIP file to free up space
rm "${NLP_LAYER_NAME}.zip"

# Deactivate virtual environment
deactivate

# Clean up
rm -rf "${TEMP_DIR}"

echo "Minimal NLP Lambda layer created successfully."