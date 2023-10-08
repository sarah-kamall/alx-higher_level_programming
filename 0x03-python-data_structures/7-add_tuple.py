#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    firstel = 0
    secel = 0
    if len(tuple_a) >= 1:
        firstel += tuple_a[0] 
    if len(tuple_a) >=2:
        secel += tuple_a[1]
    if len(tuple_b) >= 1:
        firstel += tuple_b[0]
    if len(tuple_b) >=2:
        secel += tuple_b[1]
    return (firstel, secel)
