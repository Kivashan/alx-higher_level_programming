#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    num = 0
    for i in str:
        num = ord(i)
        if (num >= 97) and (num <= 122):
            num = num - 32
        print("{}".format(chr(num)), end='')
    print()
