#!/usr/bin/python3
'''A modules containing a Student class'''


class Student:
    '''A class defining a student object'''

    def __init__(self, first_name, last_name, age):
        '''Constructor method for Student object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns a dictionary representation of a student object'''
        obj_dict = self.__dict__
        new_dict = dict()

        if isinstance(attrs, list) and len(attrs) > 0:
            for item in attrs:
                if item in obj_dict:
                    new_dict[item] = obj_dict[item]
            if len(new_dict) > 0:
                return new_dict
            return obj_dict
        else:
            return obj_dict

    def reload_from_json(self, json):
        '''Function that replaces attributes of a Student object
        it functions similar to a setter method but for dictionaries

        Args:
            json: A dictionary with the new attribute values

        Return:
            Does not return
        '''
        obj_dict = self.__dict__

        for i in json:
            obj_dict[i] = json[i]
