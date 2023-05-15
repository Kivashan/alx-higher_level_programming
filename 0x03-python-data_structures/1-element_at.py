#!/usr/bin/python3

def element_at(my_list, idx):
    length = len(my_list) - 1

    if (idx < 0) or (idx > length):
        return

    for i in range(0, length):
        if (idx == i):
            return (my_list[i])
