#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary)
    vals = map(lambda x: x * 2, list(a_dictionary.values()))
    new_dict = dict(zip(keys, vals))
    return new_dict
