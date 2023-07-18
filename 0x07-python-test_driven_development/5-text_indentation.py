#!/usr/bin/python3
'''A module containing a function that formats text'''


def text_indentation(text):
    '''Function that formats text'''
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = False    # flag variable tracks whitespace
    for alphabet in text:
        if alphabet == ' ' and flag:
            flag = False
        elif alphabet in [".", "?", ":"]:
            print(alphabet, sep='\n')
            print()
            flag = True
        else:
            print(alphabet, end="")
