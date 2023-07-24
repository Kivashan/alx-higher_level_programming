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

    def area(self):
        '''Returns the area of a Rectangle object'''
        return self.__width * self.__height

    def display(self):
        '''Displays a representation of a Rectangle object using "#" symbol'''

        [print() for row in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for column in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print()

    def __str__(self):
        '''Returns the string representation of a Rectangle object'''

        s = "[Rectangle] ({}) {}/{} - {}/{}"
        return s.format(self.id, self.__x, self.__y, self.__width,
                        self.__height)

    def update(self, *args, **kwargs):
        '''Updates Rectangle objects attributes'''

        atr = ["id", "width", "height", "x", "y"]
        if args:
            for index, value in enumerate(args):
                setattr(self, atr[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns a dictionary representation of a Rectangle object'''
        string = {"id": self.id, "width": self.width, "height": self.height,
                  "x": self.x, "y": self.y}
        return string
