#!/usr/bin/python3
"""
file 0
"""

def write_file(filename="", text=""):    
    """function to open , write to file and return num of chars written"""
    with open(filename, 'w') as file:
        data = file.write(text)
        return data

