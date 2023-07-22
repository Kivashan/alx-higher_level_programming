#!/usr/bin/python3
'''A module that contains a function that appends text to a file'''


def append_write(filename="", text=""):
    '''Appends text to a file and return the number of chars written

    Args:
        filename: The name of the file to write to
        text: The text to write to the file

    Return:
        The number of characters written to file
    '''

    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)
        return count
