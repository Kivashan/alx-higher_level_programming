#!/usr/bin/python3
'''Contains the Base class and manages the id attribute of all future
classes'''
import sys
import json


class Base:
    '''A class defining a Base class object'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor for Base class

        Args:
            id: an integer value

        Return:
            Does not return
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the json representation of list_dictionaries

        Args:
            list_dictionaries: a list of dictionaries

        Return:
            A json string representation of the argument or the string "[]"
            if empty
        '''
        if list_dictionaries is None or list_dictionaries == dict():
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves a list of objects in json represenatation to a file'''

        filename = "{}.json".format(cls.__name__)

        if list_objs is None:
            json_str = '[]'
        else:
            new_list = []
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            json_str = cls.to_json_string(new_list)

        with open(filename, "w", encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        '''Takes the json_string argument and deserializes it, the result
        should be a list of dictionaries which is returned'''

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns a new instance with all attributes set according
        to the values stored in dictionary'''

        # check if cls is an object of class Rectangle
        if cls.__name__ == "Rectangle":
            obj = cls(5, 5)

        # check if cls is an object of class Square
        if cls.__name__ == "Square":
            obj = cls(5)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''

        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, encoding='utf-8') as f:
                file_data = f.read()
                list_obj_dicts = cls.from_json_string(file_data)
                list_instances = []
                for obj in list_obj_dicts:
                    list_instances.append(cls.create(**obj))
                return list_instances

        except FileNotFoundError:
            return []
