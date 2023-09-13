#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for key, value in sorted(a_dictionary.items()):
            print(key, end=": ")
            print(value)
    else:
        return
