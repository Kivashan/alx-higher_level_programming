#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_set = set()
    total = 0
    if my_list:
        for i in my_list:
            new_set.add(i)
        for i in new_set:
            total += i
    return (total)
