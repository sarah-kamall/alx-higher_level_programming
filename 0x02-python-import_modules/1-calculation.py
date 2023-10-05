#!/usr/bin/python3
import calculator_1 as c1
def main():
    a = 10
    b = 5
    sum = c1.add(a, b)
    sub = c1.sub(a, b)
    mul = c1.mul(a, b)
    div = c1.div(a, b)
    print("{} + {} = {}".format(a, b, sum))
    print("{} + {} = {}".format(a, b, sub)) 
    print("{} + {} = {}".format(a, b, mul)) 
    print("{} + {} = {}".format(a, b, div)) 
if __name__ == "__main__":
    main()
