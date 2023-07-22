#!/usr/bin/python3
'''A module containing a function that writes to a file and returns the number
of characters written
'''


def write_file(filename="", text=""):
    '''A function that writes to a file and returns the number of bytes written

    Args:
        filename: The name of the file to write to
        test: The text to write to the file

    Return:
        Number of bytes written
    '''

    with open(filename, 'w', encoding='utf-8') as f:
        count = f.write(text)
        return count
