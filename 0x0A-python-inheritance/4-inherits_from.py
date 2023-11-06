#!/usr/bin/python3
""" 
File with one func
"""

def inherits_from(obj, a_class):
    """ function returns true if obj is same type of class"""
    return(type(obj) != a_class and isinstance(obj, a_class))
