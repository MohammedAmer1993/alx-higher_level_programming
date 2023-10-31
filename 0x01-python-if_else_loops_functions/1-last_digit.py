#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    z = number * -1
else:
    z = number
if z % 10 > 5:
    print(f"Last digit of {number} is {z % 10} and is greater than 5")
elif z % 10 == 0:
    print(f"Last digit of {number} is {z % 10} and is zero")
elif z % 10 < 5:
    print(f"Last digit of {number} is {z % 10} and is less than 6 and not 0")
