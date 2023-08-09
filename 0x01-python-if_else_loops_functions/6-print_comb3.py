#!/usr/bin/python3
for n1 in range(10):
    for n2 in range(n1, 10):
        if n1 == n2:
            pass
        else:
            if n1+2 == 10 and n2+1 == 10:
                print('{}{}'.format(n1, n2))
            else:
                print('{}{}'.format(n1, n2), end=', ')
