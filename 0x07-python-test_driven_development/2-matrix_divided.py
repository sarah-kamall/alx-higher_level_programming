#!/usr/bin/python3
""" module to divide matrix by a certain number"""

def matrix_divided(matrix, div):
    """
    function to divide each elemnt in matrix by div
    """
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
         raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(x/div, 2) for x in row] for row in matrix]
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
