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
    def to_json(self, attrs=None) :
        """returns dict of class obj"""
        string= self.__dict__
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """load and update from json"""
        for k in json:
            try:
                setattr(self, k, json[k])
            except:
                pass

