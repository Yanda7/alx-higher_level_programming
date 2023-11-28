#!/usr/bin/python3
for alphabet in range(9):
    for j in range(alphabet + 1, 10):
        if alphabet * 10 + j < 89:
            print("{:d}{:d}".format(alphabet, j), end=", ")
print("{:d}".format(89))
