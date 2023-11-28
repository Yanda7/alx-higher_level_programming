#!/usr/bin/python3
import random

def last_digit(number):
    digit = abs(number) % 10
    if number < 0:
        digit = -digit
    return digit

number = random.randint(-10000, 10000)
digit = last_digit(number)

comparisons = {
    6: "greater than 5",
    5: "equal to 5",
    0: "0",
    -5: "less than 5 and negative",
    -6: "less than 6 and not 0"
}

print("Last digit of {} is {} and is ".format(number, digit), end="")
print(comparisons[digit])
