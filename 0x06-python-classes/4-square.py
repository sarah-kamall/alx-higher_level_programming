#!/usr/bin/python3
class Square:
    def __init__(self, sizel = 0):
        self.__size = None
        self.size = sizel
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, nsize):
        if not isinstance(nsize, int):
            raise TypeError("size must be an integer")
        if nsize < 0:
            raise ValueError("size must be >= 0")
        self.__size = nsize

    def area(self):
        return self.__size **2
