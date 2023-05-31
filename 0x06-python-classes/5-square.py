#!/usr/bin/python3

'''Defining a Square class'''


class Square:
    '''A class defining a square(Geometric shape)'''

    def __init__(self, size=0):
        '''Instantiating an object of the square class
        Args:
            param1: first parameter
        '''
        self.size = size

    @property
    def size(self):
        '''Getter method for attribute size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Setter method for attribute size'''
        if ((type(value) == str) or (type(value) == float)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Method that calculates the area of a square'''
        return (self.__size * self.__size)

    def my_print(self):
        '''Prints the character # to reperesent the square'''
        row = 0
        if (self.__size == 0):
            print()
        else:
            while (row < self.__size):
                column = 0
                while (column < self.__size):
                    print("#", end="")
                    column += 1
                print()
                row += 1
