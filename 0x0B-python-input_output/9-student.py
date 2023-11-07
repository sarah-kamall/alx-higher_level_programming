#!/usr/bin/python3
"""my class file
"""
class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
         """Initializes the student"""
         self.first_name = first_name
         self.last_name = last_name
         self.age = age
    def to_json(self):
        """returns dict of class obj"""
        return self.__dict__


