#!/usr/bin/python3
'''A module containing a class MyInt, inheriting from the int class'''


class MyInt(int):
    '''A class defning a MyInt object'''

    def __eq__(self, value):
        '''overriding method for __eq__'''
        return self is value

    def __ne__(self, value):
        '''overriding method for __ne__'''
        return not (self is value)
