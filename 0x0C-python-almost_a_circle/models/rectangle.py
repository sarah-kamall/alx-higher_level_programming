#!/usr/bin/python3
"""defines rectangle class"""
from models.base import Base


class Rectangle(Base):
    """represents rectangle"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
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

