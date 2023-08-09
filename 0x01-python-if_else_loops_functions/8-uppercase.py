#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print('{}'.format('\n'))
        return

    i = 0
    while i < len(str):
        if str[i] >= 'a' and str[i] <= 'z':
            upper = chr(ord(str[i]) - 32)
        print('{}'.format(upper if 'a' <= str[i] <= 'z' else str[i]),
              end='' if i + 1 != len(str) else '\n')
        i += 1
