#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"
try:
    load_from_json_file(filename)
except FileNotFoundError:
    mylist = []
for i in argv[1: ]:
    mylist.append(i)
save_to_json_file(mylist, filename)

