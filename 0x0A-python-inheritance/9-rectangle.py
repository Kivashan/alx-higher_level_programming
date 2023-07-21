#!/usr/bin/python3
'''A module containing a class Rectangle'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''A class defining a rectangle object, inheriting from BaseGeometry'''

    def __init__(self, width, height):
        '''Contructor method for Rectangle object'''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Returns the area of the Rectangle object'''

        return self.__width * self.__height

    def __str__(self):
        '''Returns a string representation of the Rectangle object'''

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
