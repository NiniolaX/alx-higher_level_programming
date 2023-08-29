#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        item_count = 0
        for item in my_list:
            print(item, end="")
            item_count = item_count + 1
    except IndexError:
        pass
    finally:
        print()
        return item_count
