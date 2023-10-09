#!/usr/bin/python3
""" Base class of list"""


class MyList(list):
    """ class with the methon sorted"""

    def print_sorted(self):
        """print a list in sorted ascending order"""
        print(sorted(self))
