#!/usr/bin/python3
for i in range(0, 10):
    for j in range (0, 10):
        if i != 9 or j != 9:
            print("{:02d}, ".format(i * 10 + j), end = "")
        else:
            print("{:02d}".format(i * 10 + j))
