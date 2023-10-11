#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmat = [[0 for _ in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            newmat[i][j]=matrix[i][j] **2
    return newmat
