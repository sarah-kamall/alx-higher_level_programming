#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmat=matrix.copy()
    for i in newmat:
        for j in i:
            j = j*j
    return newmat
