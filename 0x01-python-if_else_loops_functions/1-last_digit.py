#!/usr/bin/python3
import random
digit = random.randint(-10000, 10000)
if digit < 0:
    last_num = digit % -10
elif number >= 0:
    last_num = digit % 10
if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
else:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
