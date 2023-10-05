#!/usr/bin/python3
import sys
def main():
    numargs = len(sys.argv) - 1
    if numargs > 0:
        print("{} arguments:".format(numargs))
    else:
        print("{} arguments.".format(numargs))
    for i in range(1, numargs + 1):
        print("{}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    main()
