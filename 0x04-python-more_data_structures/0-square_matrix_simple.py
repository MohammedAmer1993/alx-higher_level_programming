#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    myMatrix = matrix.copy()
    for i in range(len(matrix)):
        myMatrix[i] = [list(map(lambda x: x ** 2, i)) for i in matrix]
        return (myMatrix)
