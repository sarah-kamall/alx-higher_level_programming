#!/usr/bin/python3
import urllib
import sys
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
if len(sys.argv) < 2:
    exit(-1)
url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers['X-Request-Id'])
