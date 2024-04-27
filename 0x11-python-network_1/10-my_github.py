#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth =HTTPBasicAuth(sys.argv[1],sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))
