#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1,
                  'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    total = 0
    i = 0

    while i < len(roman_string):
        current_value = roman_dict.get(roman_string[i])
        if i < len(roman_string) - 1:
            next_value = roman_dict.get(roman_string[i + 1])

            if current_value < next_value:
                total += next_value - current_value
                i += 2
            else:
                total += current_value
                i += 1
        else:
            total += current_value
            i += 1

    return total
