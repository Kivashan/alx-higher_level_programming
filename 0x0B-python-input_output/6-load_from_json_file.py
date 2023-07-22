#!/usr/bin/python3
'''A function that creates an object from a JSON file'''
import json


def load_from_json_file(filename):
    '''A function that reads from a file and creates an object
    from a Json file

    Args:
        filename: The name of the file to read from

    Return:
        a py object
    '''

    with open(filename, encoding='utf=8') as f:
        return json.loads(f.read())
