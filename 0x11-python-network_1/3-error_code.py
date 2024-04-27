#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
import urllib
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            decoded_body = body.decode('utf-8')
            print(decoded_body)
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
