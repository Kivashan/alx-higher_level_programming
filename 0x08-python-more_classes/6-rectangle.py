#!/usr/bin/python3

'''A class defining a Rectangle'''


class Rectangle:
    '''A class that defines a resctangle(Geometric shape)'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Instantiating an object of the rectangle class'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        '''Deletion of an object'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        '''Getter method for the width attribute'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''Setter method for the width attribute'''
        if isinstance(value, str):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Getter method for the height attribute'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''Setter method for the height attribute'''
        if isinstance(value, str):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Returns the area of a rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Returns the perimeter of a rectangle, 0 if not arectangle'''
        for i in (self.__width, self.__height):
            if i == 0:
                return (0)
        return (2 * (self.__width + self.__height))

    def __repr__(self):
        '''Returns a formal string representation of the object'''
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __str__(self):
        '''Returns an informal string representation of the object'''
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string = string + "#"
            if i < (self.__height - 1):
                string = string + "\n"
        return (string)
