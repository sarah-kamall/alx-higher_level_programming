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
    response = requests.get(url)
    print(dict(response.headers).get('X-Request-Id'))
