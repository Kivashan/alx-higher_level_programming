#!/usr/bin/python3
'''A module containing a Square class, inheriting from Rectangle'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''A class defining a Square object'''

    def __init__(self, size):
        '''Constructor method for Square class

        Args:
            size: An integer value
        '''

        self.integer_validator("size", size)
        self.__size = size

        # calling constructor of Rectangle class
        super().__init__(size, size)

    def area(self):
        '''Returns the area of a Square object'''
        return self.__size * self.__size

    def __str__(self):
        '''Returns a string representation of a Square object'''
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
