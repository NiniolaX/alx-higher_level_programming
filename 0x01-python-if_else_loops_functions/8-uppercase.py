#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        if str[i] >= 'a' and str[i] <= 'z':
            u = ord(str[i]) - 32
            print('{}'.format(chr(u)), end='' if i + 1 != len(str) else '\n')
        else:
            print('{}'.format(str[i]), end='' if i + 1 != len(str) else '\n')
        i += 1
