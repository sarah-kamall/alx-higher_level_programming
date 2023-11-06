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
            errstr = f"{name} must be an integer"
            raise Exception(errstr)
        if value <= 0:
            errstr = f"{name} must be greater than 0"
            raise Exception(errstr)

