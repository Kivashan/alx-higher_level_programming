#!/usr/bin/python3
'''A class defining a square'''


class Square:
    '''A class defining a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Instantiation of a square object'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Getter method for size attribute'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Setter method for size attribute'''
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        '''Getter method for position attribute'''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''Setter method for position attribute'''
        msg = "position must be a tuple of 2 positive integers"
        if (type(value) != tuple or len(value) != 2):
            raise TypeError(msg)
        elif (type(value[0]) == int and type(value[1]) == int):
            if (value[0] < 0 or value[1] < 0):
                raise TypeError(msg)
            else:
                self.__position = value
        else:
            raise TypeError(msg)

    def area(self):
        '''Method that returns the area of a square'''
        return (self.__position * self.__position)

    def my_print(self):
        '''Prints the size of the square using the character #'''
        if self.__size == 0:
            print()
        else:
            row = 0
            while (row < self.__size):
                [print(" ", end="") for d in range(self.__position[0])]
                [print("#", end="") for d in range(self.__size)]
                print()
                row += 1
