#!/usr/bin/python3
"""
file 0
"""

def append_write(filename="", text=""):
    """function to open , write to file and return num of chars written"""
    with open(filename, 'a') as file:
        data = file.write(text)
        return data

