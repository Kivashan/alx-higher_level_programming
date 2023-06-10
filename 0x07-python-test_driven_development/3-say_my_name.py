#!/usr/bin/python3
'''Module contains a function that prints a given first name and last name'''


def say_my_name(first_name, last_name=""):
    '''A function that prints a string containing first name and last name'''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is " + first_name + " " + last_name)
