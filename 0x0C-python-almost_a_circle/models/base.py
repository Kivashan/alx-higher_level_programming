#!/usr/bin/python3
'''Contains the Base class and manages the id attribute of all future
classes'''


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
