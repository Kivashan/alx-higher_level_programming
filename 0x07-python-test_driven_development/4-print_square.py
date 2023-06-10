#!/usr/bin/python3
'''A module containing a function that prints a square'''


def print_square(size):
    '''Function prints a square of the given size'''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    for row in range(size):
        [print("#", end="") for column in range(size)]
        print()
