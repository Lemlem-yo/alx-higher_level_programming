#!/usr/bin/python3e
def uniq_add(my_list=[]):
    set_list = list(set(my_list))
    sum = 0
    for i in set_list:
        sum += i
    return sum
