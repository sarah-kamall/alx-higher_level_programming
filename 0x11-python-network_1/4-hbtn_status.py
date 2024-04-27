#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
import requests
if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    body = response
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
