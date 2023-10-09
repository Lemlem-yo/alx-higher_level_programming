#!/usr/bin/python3
""" inherits_from"""


def inherits_from(obj, a_class):
    """check is a sub class or not"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
