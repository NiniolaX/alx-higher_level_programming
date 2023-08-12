#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Invalid number if args
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    # Define operator and operands
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # For addition
    if operator == '+':
        print('{} {} {} = {}'.format(a, operator, b, add(a, b)))
        sys.exit(0)

    # For subtraction
    elif operator == '-':
        print('{} {} {} = {}'.format(a, operator, b, sub(a, b)))
        sys.exit(0)

    # For multiplication
    elif operator == '*':
        print('{} {} {} = {}'.format(a, operator, b, mul(a, b)))
        sys.exit(0)

    # For division
    elif operator == '/':
        print('{} {} {} = {}'.format(a, operator, b, div(a, b)))
        sys.exit(0)

    # For unknown operator
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
