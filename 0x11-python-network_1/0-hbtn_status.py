#!/usr/bin/python3
import urllib
import urllib.request


"""
Python script that fetches https://alx-intranet.hbtn.io/status
Here's what happens when you use a with statement:

The expression (e.g., opening a file, making a network request) is evaluated.
The as keyword is used to assign the result of the expression to a variable.
The code block under the with statement is executed.
After the code block completes execution, the resources associated with
the expression are automatically released or closed
regardless of whether an exception occurs.
"""

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    body_decoded = body.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body_decoded)
