#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        modifed_list = my_list.copy()
        modifed_list[idx] = element
        return modifed_list
