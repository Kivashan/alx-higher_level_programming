#!/usr/bin/python3
'''A module containing a function, "is_kind_of_class"'''


def is_kind_of_class(obj, a_class):
    '''Checks if an object is an instance of a class

    Args:
        obj: The given object
        a_class: The class

    Return:
        True if obj is an instance of a_class, False otherwise
    '''
    if isinstance(obj, a_class):
        return True
    return False
