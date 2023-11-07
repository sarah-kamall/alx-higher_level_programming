#!/usr/bin/python3
"""
file 0
"""

import json

def load_from_json_file(filename):
    """function to open , red from file and print"""
    with open(filename, 'r') as file:
        data = file.read()
        obj = json.loads(data)
        return obj

