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
        return self.__size * self.__size
