#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    else:
        last_element = my_list.pop()
        print("{:d}".format(last_element))
        print_reversed_list_integer(my_list)
