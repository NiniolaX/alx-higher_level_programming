#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        item_count = 0
        for i in range(x):
            print(my_list[i], end="")
            item_count = item_count + 1
            i = i + 1
    except IndexError:
        pass
    finally:
        print()
        return item_count
