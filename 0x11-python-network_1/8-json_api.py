#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
import sys
import requests
if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    data = {'q': letter}
    try:
        response = requests.post(url, data)
        if response.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.json().get("id"), response.json().get("name")))
    except ValueError:
        print("Not a valid JSON")
