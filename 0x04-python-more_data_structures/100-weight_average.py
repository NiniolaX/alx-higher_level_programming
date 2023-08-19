#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_of_weighted_scores = 0
    sum_of_weights = 0

    for tup in my_list:
        sum_of_weighted_scores += tup[0] * tup[1]
        sum_of_weights += tup[1]

    return sum_of_weighted_scores / sum_of_weights
