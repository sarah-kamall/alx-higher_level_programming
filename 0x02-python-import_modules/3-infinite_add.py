#!/usr/bin/python3
import sys
def main():
    numargs = len(sys.argv) - 1
    summ = 0
    for i in range(1, numargs + 1):
        summ += int(sys.argv[i])
    print("{}".format(summ))
if __name__ == "__main__":
    main()
