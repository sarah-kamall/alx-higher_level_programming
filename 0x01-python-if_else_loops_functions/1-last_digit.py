#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdig = -1 *((-1 * number) % 10)
else:
    lastdig = number % 10
if lastdig > 5:
    print(f"Last digit of {number} is {lastdig} and is greater than 5")
elif lastdig == 0:
    print(f"Last digit of {number} is {lastdig} and is 0")
else:
    print(f"Last digit of {number} is {lastdig} and is less than 6 and not 0")

