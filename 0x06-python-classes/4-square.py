#!/usr/bin/python3
"""Define a class Square"""
class Square:
    """Represent square"""
    def __init__(self, sizel = 0):
        """Initialize a new Square.
        
        Args:
            sizel (int): The size of the new square.
        """
        self.__size = None
        self.size = sizel
    
    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, nsize):
        if not isinstance(nsize, int):
            raise TypeError("size must be an integer")
        if nsize < 0:
            raise ValueError("size must be >= 0")
        self.__size = nsize

    def area(self):
        """Return the current area of the square."""
        return self.__size **2
