#!/usr/bin/python3
'''A module containing a function that returns a py oject represented
by a JSON string
'''
import json


def from_json_string(my_str):
    '''A function that returns a py object represented by a
    JSON string

    Args:
        my_str: The string representation on an object
    '''

    return json.loads(my_str)
