#!/usr/bin/python3
"""
my file
"""
import json

def save_to_json_file(my_obj, filename):
    """function to make a json string from obj and write to file"""
    stri = json.dumps(my_obj)
    with open(filename, 'a') as file:
        file.write(stri)

