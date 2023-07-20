#!/usr/bin/python3
'''A module containing a function is_same_class'''


def is_same_class(obj, a_class):
    '''Function that checks if a given object isan instacne of a given class

    Args:
        obj: The given object/instance
        a_class: The class

    Return:
        True if obj is an exact instance/subclass of a_class, False otherwise
    '''
    if type(obj) is a_class:
        return True
    return False
