#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """Represent a square."""
    def __init__(self, sizel = 0, pos= (0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = sizel
        self.position = pos

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, position):
        if (isinstance(position, tuple) or 
                len(position) == 2):
            if (isinstance(position[0], int) and 
                    isinstance(position[1], int) and
                    position[0] >= 0 and
                    position[1] >= 0):
                self.__position = position
            else:
                raise TypeError("position must be a tuple of 2 positive integers")

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

    def my_print(self):
        """Print the square with the # character."""
        if (self.__size == 0):
            print("")
            return
        for k in range(0, self.__position[1]):
            print("")
        for i in range(self.__size):
            for o in range(0, self.__position[0]):
                print(" ", end = "")
            for j in range(self.__size):
                print("#", end = "")
            print("")
