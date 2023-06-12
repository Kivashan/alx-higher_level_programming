#!/usr/bin/python3
'''A module that contains a function called lookup that
   lists all the methods and attributes within a class'''


def lookup(obj):
    '''Returns a list of the available attributes and methods of a class'''

    return (dir(obj))
