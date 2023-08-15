#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):

    add = magic_calculation_102.add
    sub = magic_calculation_102.sub

    if a < b:
        c = add(b, a)
        for i in range(4, 90, 6):
            c = add(c, i)
        return c
    else:
        return sub(b, a)

    return 0
