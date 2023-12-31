#!/usr/bin/python3
""" 
class Mylist that inherits from list
"""


class MyList(list):
    """
    Implements sorted printing for the built-in list class.
    """ 
    def __init__(self):
        """initialize base class"""
        super().__init__()
    
    def print_sorted(self):
        """sorts and prints list"""
        print(sorted(self))
