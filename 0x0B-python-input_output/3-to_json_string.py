#!/usr/bin/python3
'''A module that contains a function that returns the JSON representation
 of an object (string)
'''
import json


def to_json_string(my_obj):
    '''Function that returns the json representation of an object'''

    return json.dumps(my_obj)
