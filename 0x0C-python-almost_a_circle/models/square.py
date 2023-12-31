#!/usr/bin/python3
"""defines rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represents rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
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
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """overriding str func"""
        string = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
        return string

    def update(self, *args, **kwargs):
        """use args"""
        a = 0
        if args and len(args) != 0:
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    self.id = arg
                elif a == 1:
                    self.height = arg
                    self.width = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k,v in kwargs.items():
                if k == "id":
                    if v == None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.height = v
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self,value):
        self.width = value
        self.height = value
    
    def to_dictionary(self):
        """sq rep dict"""
        dicti = {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
        return dicti
