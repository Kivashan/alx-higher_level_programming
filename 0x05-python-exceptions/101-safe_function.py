#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except (NameError, TypeError, IndexError, ValueError) as ntiv:
        print("Exception: {}".format(ntiv), file=sys.stderr)
        return (None)
    except (ZeroDivisionError) as ntiv:
        print("Exception: {}".format(ntiv), file=sys.stderr)
        return (None)
