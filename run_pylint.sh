#!/bin/bash

# Check if a directory is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

DIRECTORY=$1

# Check if the provided argument is a directory
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: $DIRECTORY is not a directory."
    exit 1
fi

# Find all Python files in the directory and its subdirectories
PYTHON_FILES=$(find "$DIRECTORY" -name "*.py")

# Check if there are any Python files found
if [ -z "$PYTHON_FILES" ]; then
    echo "No Python files found in $DIRECTORY"
    exit 0
fi

# Run pylint on each Python file
for FILE in $PYTHON_FILES; 
do
    echo "Running pylint on $FILE"
    pylint "$FILE"
done

