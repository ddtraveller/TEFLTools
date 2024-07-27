#!/bin/bash

set -ex

# Start the JSON file
echo '{
  "files": [' > files.json

# Process each line of the input file
awk -F'Readings/' '{
    # Extract the file path
    file_path = $2
    # Remove the file size and date from the beginning
    sub(/^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} +[0-9]+ +/, "", file_path)
    # Print the JSON entry
    printf "    {\n"
    printf "      \"path\": \"Readings/%s\",\n", file_path
    printf "      \"size\": %d\n", $1
    printf "    },"
}' list.txt >> files.json

# Remove the trailing comma from the last entry
sed -i '$ s/,$//' files.json

# Close the JSON file
echo '
  ]
}' >> files.json

# Pretty-print the JSON (requires jq)
if command -v jq &> /dev/null; then
    jq '.' files.json > temp.json && mv temp.json files.json
fi

echo "files.json has been created."