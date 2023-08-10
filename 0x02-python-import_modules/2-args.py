#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ac = len(sys.argv)
    print('{} {}{}'.format(ac - 1, 'argument' if ac - 1 == 1 else 'arguments',
                           '.' if ac - 1 == 0 else ':'))
    for a in range(1, ac):
        print('{}: {}'.format(a, sys.argv[a]))
        a += 1
