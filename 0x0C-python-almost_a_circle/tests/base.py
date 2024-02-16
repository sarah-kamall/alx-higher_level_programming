#!/usr/bin/python3
"""
base file
"""
import json
class Base:
    """
    class base
    """
    __nb_objects = 0
    """constructor priv"""
    def __init__(self, id=None):
        if id != None:
            self.id = id;
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """
	        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
