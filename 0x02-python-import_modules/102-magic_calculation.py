#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    add = magic_calculation_102.add
    sub = magic_calculation_102.sub

    if a < b:
        c = add(a, b)
        for i in range(4, 90, 6):
            c = add(c, i)
        return c
    else:
        return sub(b, a)

    return 0