#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedlist=sorted(a_dictionary.keys())
    for i in sortedlist:
        print("{}: {}".format(i,a_dictionary[i]))
