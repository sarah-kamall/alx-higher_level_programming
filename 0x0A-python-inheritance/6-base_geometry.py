#!/usr/bin/python3
"""
file with base class Base Geometery
"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        """raising exception if area isnt implemented"""
        raise Exception("area() is not implemented")
