#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
