#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    num = 0
    for i in str:
        num = ord(i)
        if (num >= 65) and (num <= 90):
            new_str += i
        elif (num >= 97) and (num <= 122):
            new_str += (chr(num - 32))
        else:
            new_str += i
    print(new_str)
