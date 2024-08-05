#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -ex

# Update package list and install required packages
sudo apt-get update
sudo apt-get install -y curl apt-transport-https ca-certificates gnupg

# Add the Google Cloud SDK distribution URI as a package source
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Import the Google Cloud public key
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

# Update and install the Google Cloud SDK
sudo apt-get update && sudo apt-get install -y google-cloud-sdk

# Initialize gcloud
gcloud init --console-only

# Set up application default credentials
gcloud auth application-default login

echo "Google Cloud SDK has been installed and initialized."
echo "You may need to restart your terminal or run 'source ~/.bashrc' to use gcloud commands."