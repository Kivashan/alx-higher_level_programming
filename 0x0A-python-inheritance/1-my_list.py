#!/usr/bin/python3
'''A module containing a class MyList that inherits from class list'''


class MyList(list):
    '''Class defining an object of MyList, inherits from class list'''

    def print_sorted(self):
        '''Prints a list in ascending order'''
        copy = self.copy()
        copy.sort()
        print(copy)
