#!/usr/bin/python3
import sys


def factorize(digits):
    """ factors for a provided digit """
    elem1 = 2
    while (digits % elem1):
        if (elem1 <= digits):
            elem1 += 1

    elem2 = digits // elem1
    return (elem2, elem1)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()

for line in lines:
    digits = int(line.rstrip())
    elem2, elem1 = factorize(digits)
    print(f"{digits} = {elem2} * {elem1}")
