#!/bin/bash
set -ex

# Set variables
MAIN_LAYER_NAME="anthropic-llm-mother-earth-news"
ADDITIONAL_LAYER_NAME="additional-dependencies"
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

# Function to create and publish a layer
create_layer() {
    local LAYER_NAME=$1
    local LAYER_DESC=$2
    local LAYER_DIR="${TEMP_DIR}/${LAYER_NAME}"
    
    mkdir -p "${LAYER_DIR}/python"
    
    # Install packages
    pip install ${@:3} --target "${LAYER_DIR}/python" --upgrade --no-cache-dir
    
    # Create ZIP file
    cd "${LAYER_DIR}"
    zip -r "${LAYER_NAME}.zip" python
    
    # Publish layer
    LAYER_ARN=$(aws lambda publish-layer-version \
        --layer-name "${LAYER_NAME}" \
        --description "${LAYER_DESC}" \
        --license-info "MIT" \
        --zip-file "fileb://${LAYER_NAME}.zip" \
        --compatible-runtimes "${RUNTIME}" \
        --query 'LayerVersionArn' \
        --output text)
    
    echo "${LAYER_NAME} ARN: ${LAYER_ARN}"
    
    # Remove the ZIP file to free up space
    rm "${LAYER_NAME}.zip"
}

# Create main application layer
create_layer "${MAIN_LAYER_NAME}" "Layer for Anthropic LLM Mother Earth News application" \
    anthropic==0.2.8 \
    tiktoken==0.3.3 \
    openai==0.27.0 \
    boto3==1.28.38 \
    requests==2.31.0 \
    google-auth==2.22.0 \
    google-auth-oauthlib==1.0.0

# Create additional dependencies layer
create_layer "${ADDITIONAL_LAYER_NAME}" "Layer for additional dependencies" \
    aiohttp==3.8.4 \
    multidict==6.0.4 \
    attrs==23.1.0 \
    yarl==1.9.2 \
    idna==3.4 \
    chardet==5.1.0 \
    async-timeout==4.0.2 \
    frozenlist==1.3.3 \
    aiosignal==1.3.1 \
    urllib3==1.26.16 \
    botocore==1.31.38 \
    jmespath==0.10.0 \
    s3transfer==0.6.1 \
    python-dateutil==2.8.2 \
    six==1.16.0 \
    tqdm==4.65.0 \
    charset-normalizer==2.0.12

# Deactivate virtual environment
deactivate

# Clean up
rm -rf "${TEMP_DIR}"

echo "Main and additional Lambda layers created and published successfully."