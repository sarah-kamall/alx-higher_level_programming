#!/usr/bin/python3
"""
file that has class square
"""

Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    
    """class square that inherits from rectangle"""

    def __init__(self, size):
        """square initializer"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def area(self):
        """calculates area"""
        return self.__size **2

