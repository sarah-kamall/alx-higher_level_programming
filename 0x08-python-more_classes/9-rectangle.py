#!/usr/bin/python3
"""file containing a class Rectangle"""


class Rectangle:
    """Represent a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"
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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """function calculating area"""
        return self.width * self.height

    def perimeter(self):
        """fuction calculating premiter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """make a string representation of rectangle using #"""
        stringr = ""
        if self.width == 0:
            return stringr
        for i in range(self.height):
            stringr += str(self.print_symbol) * self.width
            if i != self.height - 1:
                stringr += "\n"
        return stringr

    def __repr__(self):
        """make a code string to feed to eval to create a new rectangle"""
        stringt = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return stringt

    def __del__(self):
        """class destructor """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area""" 
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.
        Args:
            size (int): The width and height of the new Rectangle.
        """
        rect = Rectangle(size, size)
        return rect
    pass
