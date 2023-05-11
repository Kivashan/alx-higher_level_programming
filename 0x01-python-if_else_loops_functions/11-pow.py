#!/usr/bin/python3
def pow(a, b):
    retval = a
    i = 0
    c = 0

    if (b == 0):
        c = 0
    elif (b < 0):
        c = -b - 1
    else:
        c = b - 1

    while (i < c):
        retval = retval * a
        i += 1
    if (b >= 0):
        return (retval)
    return (1 / retval)
