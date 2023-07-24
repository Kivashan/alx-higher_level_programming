#!/usr/bin/python3
'''A module containing the Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A class defining a Rectangle object, inherits from Base class'''

    type_err_msg = "%s must be an integer"
    value_err_msg = "%s must be > 0"
    value_err_msg_xy = "%s must be >= 0"

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
    def width(self, value):
        '''Setter method for width attribute'''
        if not isinstance(value, int):
            raise TypeError(Rectangle.type_err_msg % "width")
        elif value <= 0:
            raise ValueError(Rectangle.value_err_msg % "width")
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
            raise TypeError(Rectangle.type_err_msg % "height")
        elif value <= 0:
            raise ValueError(Rectangle.value_err_msg % "height")
        else:
            self.__height = value

    @property
    def x(self):
        '''Getter method for x attribute'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter method for x attribute'''
        if not isinstance(value, int):
            raise TypeError(Rectangle.type_err_msg % "x")
        elif value < 0:
            raise ValueError(Rectangle.value_err_msg_xy % "x")
        else:
            self.__x = value

    @property
    def y(self):
        '''Getter method for y attribute'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter method for y attribute'''
        if not isinstance(value, int):
            raise TypeError(Rectangle.type_err_msg % "y")
        elif value < 0:
            raise ValueError(Rectangle.value_err_msg_xy % "y")
        else:
            self.__y = value
