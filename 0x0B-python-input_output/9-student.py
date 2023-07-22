#!/usr/bin/python3
'''A modules containing a Student class'''


class Student:
    '''A class defining a student object'''

    def __init__(self, first_name, last_name, age):
        '''Constructor method for Student object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''returns a dictionary representation of a student object'''

        return self.__dict__
