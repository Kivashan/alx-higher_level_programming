#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string:
        length = len(my_string)
        i = 0
        while i < length:
            if (my_string[i] != 'c') and (my_string[i] != 'C'):
                new_string += my_string[i]
            i += 1
        return (new_string)
   return (my_string)
