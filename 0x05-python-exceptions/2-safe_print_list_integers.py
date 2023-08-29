#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    item_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            item_count = item_count + 1
        except (TypeError, ValueError):
            pass
        finally:
            i = i + 1
    print()
    return item_count
