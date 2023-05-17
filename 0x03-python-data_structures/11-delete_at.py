#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if my_list:
        length = len(my_list) - 1
        if idx >= 0 and idx <= length:
            del my_list[idx]
        return (my_list)
    return (my_list)
