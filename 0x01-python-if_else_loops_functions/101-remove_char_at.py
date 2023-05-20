#!/usr/bin/python3

def remove_char_at(str, n):
    count = 0
    new_str = ""
    for i in str:
        if count != n:
            new_str += i
        count += 1
    return (new_str)
