#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    return_val = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return_val = False
    finally:
        return return_val
