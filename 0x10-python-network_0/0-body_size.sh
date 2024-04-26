#!/bin/bash/
#comment?

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the provided URL and store the response body in a temporary file
response=$(curl -s -o /tmp/response_body "$1")

# Check if curl encountered an error
if [ $? -ne 0 ]; then
    echo "Error: Failed to send request to $1"
    exit 1
fi

# Get the size of the response body in bytes
body_size=$(stat -c %s /tmp/response_body)

# Display the size of the response body
echo $body_size 

# Remove the temporary file
rm -f /tmp/response_body
