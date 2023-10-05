#!/usr/bin/python3
import calculator_1 as c1
def main():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, c1.add(a, b)))
    print("{} + {} = {}".format(a, b, c1.sub(a, b))) 
    print("{} + {} = {}".format(a, b, c1.mul(a, b))) 
    print("{} + {} = {}".format(a, b, c1.div(a, b))) 
if __name__ == "__main__":
    main()
