#!/bin/bash
set -e
set -x

LAYER_NAME="english-tetum-translator-deps"
S3_BUCKET="tl-web"
REQUIREMENTS_FILE="requirements.txt"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Create a temporary directory
TEMP_DIR=$(mktemp -d)
echo "Created temporary directory: $TEMP_DIR"

# Create the structure for the Lambda layer
mkdir -p "$TEMP_DIR/python"

# Install dependencies
pip install -r "$SCRIPT_DIR/$REQUIREMENTS_FILE" -t "$TEMP_DIR/python" --no-cache-dir

# Remove unnecessary files and directories
find "$TEMP_DIR/python" -type d -name "tests" -exec rm -rf {} +
find "$TEMP_DIR/python" -type d -name "test" -exec rm -rf {} +
find "$TEMP_DIR/python" -type f -name "*.pyc" -delete
find "$TEMP_DIR/python" -type f -name "*.pyo" -delete
find "$TEMP_DIR/python" -type d -name "__pycache__" -exec rm -rf {} +

# Create a ZIP file
cd "$TEMP_DIR"
zip -r9 "$SCRIPT_DIR/layer.zip" .
cd "$SCRIPT_DIR"

# Print the size of the layer
echo "Layer size: $(du -sh layer.zip | cut -f1)"

# Upload the ZIP file to S3
aws s3 cp "layer.zip" "s3://$S3_BUCKET/layer.zip"

# Update the layer
aws lambda publish-layer-version \
    --layer-name "$LAYER_NAME" \
    --description "Optimized dependencies for English-Tetum Translator" \
    --content S3Bucket="$S3_BUCKET",S3Key="layer.zip" \
    --compatible-runtimes python3.9

# Clean up
rm -rf "$TEMP_DIR" "layer.zip"

echo "Optimized Lambda layer created/updated successfully."