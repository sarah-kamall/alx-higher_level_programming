#!/usr/bin/python3
import urllib
import urllib.request
import sys
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
dict(response.headers).get('X-Request-Id')
makes a shallow copy of response.headers and returns null if key isnt found
while response.headers['key'] returns a key error !
"""
if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get('X-Request-Id'))
