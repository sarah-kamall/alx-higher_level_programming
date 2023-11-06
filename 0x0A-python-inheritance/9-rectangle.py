#!/usr/bin/python3
"""
file that has class rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """function to initialize Rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
    
    def area(self):
        """returns area"""
        return self.__width * self.__height
    
    def __str__(self):
        """return sstring rep of class"""
        string = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return string
    
