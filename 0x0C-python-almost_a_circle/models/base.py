#!/usr/bin/python3
"""
base file
"""
class Base:
    """
    class base
    """
    __nb_objects = 0
    """constructor priv"""
    def __init__(self, id=None):
        if id != None:
            self.id = id;
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects


