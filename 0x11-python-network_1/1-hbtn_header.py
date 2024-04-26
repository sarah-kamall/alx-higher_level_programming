#!/usr/bin/python3
"""
A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
dict(response.headers).get('X-Request-Id')
makes a shallow copy of response.headers and returns null if key isnt found
while response.headers['key'] returns a key error !
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get('X-Request-Id'))
This approach involves creating a Request object explicitly,
allowing you to set additional parameters such as headers, data, etc.,
 if needed, before making the request.
It provides more flexibility in customizing the request before sending it.
with urllib.request.urlopen(url) as response:
    print(dict(response.headers).get('X-Request-Id'))
This approach skips the explicit creation of a Request object
and directly opens a connection to the specified URL.
It's a more concise way to make a simple GET request without
 customizing headers or other request parameters.
"""
import urllib
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
