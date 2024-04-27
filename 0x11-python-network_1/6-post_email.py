#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
