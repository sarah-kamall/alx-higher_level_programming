#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            res += chr(ord(str[i]) - 32)
        else:
            res += str[i]
    print("{}".format(res))
