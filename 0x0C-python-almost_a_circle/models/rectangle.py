#!/usr/bin/python3
from models.base import Base
"""class rectangle"""

class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor imp"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    """setters and getters"""
    @property
    def width(self):
        """return width"""
        return self.__width
    @width.setter
    def width(self,value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__width = value
    @property
    def height(self):
        """return height"""
        return self.__height
    @height.setter
    def height(self,value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__height = value
    @property
    def x(self):
        """return x"""
        return self.__x;
    @x.setter
    def x(self,value):
        if not isinstance(value, int):
            raise TypeError
        self.__x = value
    @property 
    def y(self):
        """return y"""
        return self.__y
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError
        self.__y = value


