#!/usr/bin/python3
'''A module containing a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
'''


def class_to_json(obj):
    '''Returns a dictionary of an objects attributes'''

    if "__dict__" in dir(obj):
        obj_dict = obj.__dict__
        return obj_dict
