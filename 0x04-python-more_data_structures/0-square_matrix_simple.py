#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matric"""
    matrixSquare = [[x**2 for x in row] for row in matrix]
    return matrixSquare
