#!/usr/bin/python3
'''A module containing a Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A class defining a Square object'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor method for Square object'''

        # calling constructor of Rectangle class
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Getter method for size attribute'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter method for size attribute'''
        self.width = value
        self.height = value

    def __str__(self):
        '''Returns a string representation of a Square object'''

        s = "[Square] (%s) %s/%s - %s"
        return s % (self.id, self.x, self.y, self.width)
