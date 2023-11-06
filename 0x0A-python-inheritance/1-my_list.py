#!/usr/bin/python3
""" class Mylist that inherits from list"""

class Mylist(list):
    """Implements sorted printing for the built-in list class."""
    
    def print_sorted(self):
        """sorts and prints list"""
        
        print(sorted(self))
