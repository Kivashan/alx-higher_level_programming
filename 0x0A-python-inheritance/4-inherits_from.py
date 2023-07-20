#!/usr/bin/python3
'''A module containing a function, "inherits_from"'''


def inherits_from(obj, a_class):
    '''Tests if an obj inherited from a class, directly or indirectly

    Args:
        obj: The given object
        a_class: The class

    Return:
        True if object inherited from class, false otherwise
    '''

    if isinstance(obj, a_class) and not(type(obj) is a_class):
        return True
    return False
