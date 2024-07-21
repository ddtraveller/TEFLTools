#!/bin/bash
set -e

LAYER_NAME="english-tetum-translator-deps"
S3_BUCKET="tl-web"
TEMP_DIR=$(mktemp -d)

echo "Downloading layer..."
aws s3 cp "s3://$S3_BUCKET/layer.zip" "$TEMP_DIR/layer.zip"

echo "Extracting layer..."
unzip -q "$TEMP_DIR/layer.zip" -d "$TEMP_DIR/layer_contents"

echo "Analyzing layer contents..."
du -sh "$TEMP_DIR/layer_contents/python"/*

echo "Top 10 largest directories:"
du -h "$TEMP_DIR/layer_contents/python" | sort -rh | head -n 10

echo "Top 10 largest files:"
find "$TEMP_DIR/layer_contents/python" -type f -exec du -h {} + | sort -rh | head -n 10

rm -rf "$TEMP_DIR"