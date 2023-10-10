#!/usr/bin/python3
""" from_json_string method"""
import json


def from_json_string(my_str):
    """function:
        that return the string form json file

        Args:
                my_str: json file container
    """
    return json.loads(my_str)
