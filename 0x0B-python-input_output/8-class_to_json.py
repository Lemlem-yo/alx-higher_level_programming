#!/usr/bin/python3
""" class to JSON method"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data"""
    return obj.__dict__
