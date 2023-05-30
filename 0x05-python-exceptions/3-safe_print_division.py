#!/usr/bin/python3
def safe_print_division(a, b):
    print("Inside result: ", end="")
    try:
        answer = a / b
    except ZeroDivisionError:
        answer = None
    finally:
        print("{}".format(answer))
    return (answer)
