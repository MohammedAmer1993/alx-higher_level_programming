#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix[0]:
        for i in range(len(matrix)):
            print("{:d}".format(matrix[i][0]), end="")
            for k in range(1, len(matrix[i])):
                print(" {:d}".format(matrix[i][k]), end="")
            print()
