@echo off
setlocal

:: Define the URL and filenames
set URL=https://raw.githubusercontent.com/scanoss/purl2cpe/refs/heads/main/purl2cpe.db.zip
set ZIP_FILE=purl2cpe.db.zip
set EXTRACTED_DIR=purl2cpe.db
set FINAL_FILE=purl2cpe.db

:: Download the zip file using curl
echo Downloading %URL% ...
curl -L -o %ZIP_FILE% %URL%

:: Check if the zip file was downloaded successfully
if not exist %ZIP_FILE% (
    echo Failed to download the file!
    exit /b 1
)

:: Extract the zip file
echo Extracting %ZIP_FILE% ...
powershell -Command "Expand-Archive -Path '%ZIP_FILE%' -DestinationPath '.'"

:: Check if extraction was successful
if not exist %FINAL_FILE% (
    echo Extraction failed or target file not found!
    exit /b 1
)

echo File extracted successfully to %FINAL_FILE%

:: Clean up the zip file
del %ZIP_FILE%

endlocal
