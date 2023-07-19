#!/usr/bin/python3
'''A module containing a class that defines a Rectangle object'''


class Rectangle:
    '''A class defining a Rectangle object'''

    def __init__(self, width=0, height=0):
        '''Initialization method for a Rectangle object'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter method for width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for width attribute'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Getter method for height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for height attribute'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Method to obtain an objects area'''
        return self.__width * self.__height

    def perimeter(self):
        '''Method to obtain an objects perimeter'''
        if 0 in [self.__width, self.__height]:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        '''Method that prints a representation of the object'''
        str_rep = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str_rep = str_rep + "#"
            if i < self.__height - 1:
                str_rep = str_rep + "\n"
        return str_rep
