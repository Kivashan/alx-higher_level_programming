#!/usr/bin/python3
'''Module that contains a function that divides each
   element of a matrix by div and returns a new matrix
'''


def matrix_divided(matrix, div):
    '''A function that divides each element of a matrix by div
       and returns a new matrix
    '''

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    # checks if matrix is a list of lists containing integers or floats
    if len(matrix) == 0:
        raise TypeError(msg)
    if not isinstance(matrix, list):
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for item in row:
            if not (isinstance(item, int)) and not (isinstance(item, float)):
                raise TypeError(msg)

    msg2 = "Each row of the matrix must have the same size"
    # checks length of row in matrix, rows must be of same length
    og_length = len(matrix)
    row1_length = len(matrix[0])
    if og_length > 1:
        for row in matrix[1:]:
            if row1_length != len(row):
                raise TypeError(msg2)

    # checks for divisor
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_item = (item / div) * 100
            if new_item % 10 >= 5:
                new_item = int(new_item + 1) / 100
            else:
                new_item = int(new_item) / 100

            new_row.append(new_item)

        new_matrix.append(new_row)

    return (new_matrix)
