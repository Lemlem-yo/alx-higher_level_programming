#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    set_list = set(my_list)
    add_set = reduce(lambda x, y: x + y, set_list)
    return add_set
