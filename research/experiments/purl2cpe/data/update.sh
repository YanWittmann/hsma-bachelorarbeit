#!/bin/bash

# Define the URL and filenames
URL="https://raw.githubusercontent.com/scanoss/purl2cpe/refs/heads/main/purl2cpe.db.zip"
ZIP_FILE="purl2cpe.db.zip"
EXTRACTED_DIR="purl2cpe.db"
FINAL_FILE="purl2cpe.db"

# Download the zip file using curl
echo "Downloading $URL ..."
curl -L -o "$ZIP_FILE" "$URL"

# Check if the zip file was downloaded successfully
if [ ! -f "$ZIP_FILE" ]; then
    echo "Failed to download the file!"
    exit 1
fi

# Extract the zip file
echo "Extracting $ZIP_FILE ..."
unzip -o "$ZIP_FILE"

# Check if extraction was successful
if [ ! -f "$FINAL_FILE" ]; then
    echo "Extraction failed or target file not found!"
    exit 1
fi

echo "File extracted successfully to $FINAL_FILE"

# Clean up the zip file
rm "$ZIP_FILE"
