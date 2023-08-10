#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ac = len(sys.argv)
    args_sum = 0
    for i in range(1, ac):
        arg = int(sys.argv[i])
        args_sum += arg
        i += 1
    print(args_sum)
