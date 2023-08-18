#!/usr/bin/python3
def roman_to_int(roman_string):

    if not type(roman_string) is str:
        return 0

    if str is None or len(roman_string) == 0:
        return 0

    # Build dictionary of roman symbols
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    # Iterate to second-to-last symbol in Roman string
    for i, s in enumerate(roman_string[:-1]):
        if dict[roman_string[i + 1]] > dict[s]:
            result += -dict[s]
        else:
            result += dict[s]

    # Add value of last symbol in Roman string
    result += dict[roman_string[-1]]

    return result
