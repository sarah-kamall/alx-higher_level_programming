#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lista in matrix:
        for index ,num in enumerate(lista):
            if index != len(lista) - 1:
                print("{:d}".format(num),end = " ")
            else:
                print("{:d}".format(num),end = "")
        print()
