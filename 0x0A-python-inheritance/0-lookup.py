#!/usr/bin/python3
"""file with funcs to return list of all available attributes
"""
def lookup(obj):
    """lookup :Return a list of an object's available attributes."""
    return(dir(obj))
