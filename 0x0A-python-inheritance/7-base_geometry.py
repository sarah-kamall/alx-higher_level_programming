#!/usr/bin/python3
"""
file with base class Base Geometery
"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        """raising exception if area isnt implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """function to validate int"""
        if not isinstance(value, int):
            errstr = "{:s} must be an integer".format(name)
            raise TypeError(errstr)
        if value <= 0:
            errstr = "{:s} must be greater than 0".format(name)
            raise ValueError(errstr)

