#!/usr/bin/python3
def no_c(my_string):
    charlist = list(my_string)
    cslist = ['c', 'C']
    for index, char in enumerate(charlist):
        if char in cslist:
            charlist.pop(index)
    return (''.join(charlist))
