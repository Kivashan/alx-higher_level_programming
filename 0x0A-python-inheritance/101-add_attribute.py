#!/usr/bin/python3
'''Module contains a function that checks if we can add a new attribute
to an object
'''


def add_attribute(obj, name, value):
    '''Adds an attribute to an object if possible'''
    atts = dir(obj)
    if "__dict__" not in atts:
        raise TypeError("can't add new attribute")
    else:
        obj.name = value
