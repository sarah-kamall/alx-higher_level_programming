#!/usr/bin/python3
"""
file 0
"""

def read_file(filename=""):
    """function to open , red from file and print"""
    with open(filename, 'r') as file:
        data = file.read()
        print(data, end = "")

