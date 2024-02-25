#!/usr/bin/python3
"""Module for matrix divide all of tests are found in /tests
this module accept a matrix of int or floats and divid it by a number.
you should provide matrix in the right form and a dividor
if you didn't provide argument in the right form exception will be raised.
the dividor mustn't be zero """


def matrix_divided(matrix, div):
    """matrix_divided - divid a matrix by a num
    Args:
        matrix (list of list): the matrix
        div (int): the dividor
    Return:
        a new matrix
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif type(matrix[0]) is not list or len(matrix[0]) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    number_of_elemnts = len(matrix[0])
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        elif len(i) != number_of_elemnts:
            raise TypeError("Each row of the matrix must have the same size")
        for m in i:
            if type(m) is not int and type(m) is not float:
                raise TypeError(
                    "matrix must be a matrix "
                    + "(list of lists) of integers/floats")

    if div == float('inf') or div == -float('inf') or div != div:
        div = 10
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    my_list = []
    for i in range(len(matrix)):
        my_list.append([])
        for index in range(len(matrix[i])):
            res = round((matrix[i][index] / div), 2)
            my_list[i].append(res)

    return my_list
