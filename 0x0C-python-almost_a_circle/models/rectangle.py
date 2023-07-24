#!/usr/bin/python3
'''A module containing the Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A class defining a Rectangle object, inherits from Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor method for Rectangle class'''
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # calling constructor of Base class
        super().__init__(id)

    @property
    def width(self):
        '''Getter method for width attribute'''
        return self.__width

    @width.setter
    def width(self, width):
        '''Setter method for width attribute'''
        self.__width = width

    @property
    def height(self):
        '''Getter method for height attribute'''
        return self.__height

    @height.setter
    def height(self, height):
        '''Setter method for height attribute'''
        self.__height = height

    @property
    def x(self):
        '''Getter method for x attribute'''
        return self.__x
    @x.setter
    def x(self, x):
        '''Setter method for x attribute'''
        self.__x = x

    @property
    def y(self):
        '''Getter method for y attribute'''
        return self.__y

    @y.setter
    def y(self, y):
        '''Setter method for y attribute'''
        self.__y = y
