#!/usr/bin/python3
'''A module containing a function that returns all attributes of an object'''


def lookup(obj):
    '''A function that returns a list of the given objects attributes

    Args:
        obj: The given object

    Return:
        A list of the objects attributes
    '''
    return dir(obj)
