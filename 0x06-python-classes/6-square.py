#!/usr/bin/python3
class Square:
    def __init__(self, sizel = 0):
        self.__size = None
        self.__position = None
        self.size = sizel

    @property
    def position(self):
        return self.__position

    @position.setter(self, position):
        if isinstance(position, tuple) or len(position) == 2:
            if isinstance(position[0], int) and isinstance(position[1], int) and position[0] >= 0 and position[1] >= 0:
                self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    def my_print(self):
        if (self.__size == 0):
            print("")
            return
        for k in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for o in range(self.__position[0]):
                print(" ", end = "")
            for j in range(self.__size):
                print("#", end = "")
            print("")
