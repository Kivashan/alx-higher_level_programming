#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        return (fct(*args))
    except (NameError, TypeError, IndexError, ValueError) as ntiv:
        print("Exception: {}".format(ntiv))
        return (None)
    except (ZeroDivisionError) as ntiv:
        print("Exception: {}".format(ntiv))
        return (None)
