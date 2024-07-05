#!/bin/sh

# Load environment variables from .env.app located in /mnt
set -o allexport
source /mnt/.env.core
set -o allexport

# File paths
CONFIG_FILE="/mnt/config/config-template.json"
TEMP_CONFIG_FILE="/mnt/config/config.json"

# Replace placeholders in config.json and write to the temp directory
sed -e "s|<AZURE_OPENAI_ENDPOINT>|$AZURE_OPENAI_ENDPOINT|g" \
    -e "s|<AZURE_DEPLOYMENT_OPENAI_35>|$AZURE_DEPLOYMENT_OPENAI_35|g" \
    -e "s|<AZURE_DEPLOYMENT_OPENAI_4>|$AZURE_DEPLOYMENT_OPENAI_4|g" \
    -e "s|<AZURE_DEPLOYMENT_EMBEDDING>|$AZURE_DEPLOYMENT_EMBEDDING|g" \
    -e "s|<AZURE_OPENAI_API_KEY>|$AZURE_OPENAI_API_KEY|g" \
    "$CONFIG_FILE" > "$TEMP_CONFIG_FILE"