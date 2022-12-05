#!/usr/bin/python3
""" function that replaces an element in a list at a specific"""

def new_in_list(my_list, idx, element): 
    if idx < 0 or idx > len(my_list):
        return my_list
    new = my_list.copy()
    new[idx] = element
    return new
