#!/usr/bin/python3
'''A module containing a class BaseGeometry'''


class BaseGeometry:
    '''A class defining a BaseGeometry object'''

    def area(self):
        '''Method that returns the area of the BaseGeometry object'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method that validates an integer

        Args:
            name: name of variable storing the integer value
            value: the value/integer

        Return:
            Does not return

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
