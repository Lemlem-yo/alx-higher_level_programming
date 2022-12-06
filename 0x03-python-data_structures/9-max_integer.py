#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    larger_number = my_list[0]
    for number in my_list:
        if number > larger_number:
            larger_number = number
    return larger_number
