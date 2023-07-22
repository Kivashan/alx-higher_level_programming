#!/usr/bin/python3
'''A module containing a function that reads a file'''


def read_file(filename=""):
    '''A function that reads a file and prints it to stdout

    Args:
        filename: The name of the file to read

    Return:
        No return value
    '''

    with open(filename, encoding='utf-8') as f:
        print(f.read())
