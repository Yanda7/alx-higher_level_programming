#!/usr/bin/python3
for letter in range(0, 100):
    if letter != 99:
        print("{:02d}, ".format(letter), end="")
    else:
        print("{:02d}".format(letter))
