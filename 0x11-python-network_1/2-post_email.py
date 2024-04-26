#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
 and displays the body of the response (decoded in utf-8)
"""
import urllib
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data_encoded = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, data=data_encoded)
    print(request.data)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')
        print(decoded_body)
