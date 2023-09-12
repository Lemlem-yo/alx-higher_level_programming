#!/usr/bin/python3
def element_at(my_list, idx):
    if (my_list.index(idx) < 0):
        return None
    elif (my_list.index(idx) > len(my_list)):
        return None
    else:
        return my_list[idx]
