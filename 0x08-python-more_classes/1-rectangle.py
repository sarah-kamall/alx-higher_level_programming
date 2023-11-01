#!/usr/bin/python3
"""file containing a class Rectangle"""


class Rectangle:
    """Represent a Rectangle"""
    def checkvalueintw(self, value):
        """check if value is of type int and valid dimention"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return True

    def checkvalueinth(self, value):
        """check if value is of type int and valid dimention"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return True

    def __init__(self, width=0, height=0):
        """function to initilize rectangle
        Args:
            width
            height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if (self.checkvalueintw(value)):
            self.__width = value

    @property
    def height(self):
        """get rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if(self.checkvalueinth(value)):
            self.__height = value

    pass
