#!/usr/bin/python3
'''A module containing a class, LockedClass'''


class LockedClass:
    '''Only allows the creation of the instance variable "first_name"

    uses the magic method __slots__
    '''

    __slots__ = ["first_name"]
