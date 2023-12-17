#!/usr/bin/python3
"""Contains a function that hopefully helps in preventing SQL injection"""


def validator(rows, userinput=None):
    """Takes in data stored in a database and userinput.
    Attempts  to match user data and returns a tuple containing all matches

    Args:
        a: rows from database
        b: userinput

    Return:
        Returns a tuple containing all matches on success
        Returns an empty tuple otherwise

    Note:
        This implementation is based strictly on ALX examples and must be
        modified according to how data from db is represented in program.
    """

    retval = []

    """ Return empty tuple is no user input"""
    if userinput is None:
        return retval

    """Iterate through rows and if match occurs add to retval else do
    nothing
    """
    for i in rows:
        try:
            if (i.index(userinput) >= 0):
                retval.append(i)
        except ValueError:
            pass

    return retval
