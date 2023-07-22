#!/usr/bin/python3
'''A module containing a function that writes an object to a text file
using JSON representation, encodes an object to JSON
'''
import json


def save_to_json_file(my_obj, filename):
    '''Function encodes an object to Json and then saves the Json
    representation to a Json file

    Args:
        my_obj: The object to encode to Json
        filename: The name of the file to save the Json representation

    Return:
        Does not return
    '''

    with open(filename, 'w', encoding='utf=8') as f:
        json.dump(my_obj, f)
