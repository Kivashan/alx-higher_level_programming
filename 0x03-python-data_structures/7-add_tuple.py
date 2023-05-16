#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    list_new = [0, 0]
    list_a = [*tuple_a, ]
    list_b = [*tuple_b, ]

    if len(tuple_a) < 2:
        for i in range(len(list_a), 2):
            list_a.append(0)
    if len(tuple_b) < 2:
        for i in range(len(list_b), 2):
            list_b.append(0)
    list_new[0] = list_a[0] + list_b[0]
    list_new[1] = list_a[1] + list_b[1]
    return ((list_new[0], list_new[1]))
