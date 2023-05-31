#!/usr/bin/python3

'''Defining a Square class'''


class Square:
    '''A class defining a square(Geometric shape)'''

    def __init__(self, size=0):
        '''Instantiating an object of the square class
        Args:
            param1: first parameter
        '''
        if (type(size) == str):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
