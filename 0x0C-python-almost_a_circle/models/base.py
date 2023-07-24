#!/usr/bin/python3
'''Contains the Base class and manages the id attribute of all future
classes'''
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
