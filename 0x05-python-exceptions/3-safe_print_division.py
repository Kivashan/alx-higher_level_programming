#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        answer = a / b
        print("Inside result: {}".format(answer))
        return (answer)
    except ZeroDivisionError:
        print("Inside result: None")
        return (None)
