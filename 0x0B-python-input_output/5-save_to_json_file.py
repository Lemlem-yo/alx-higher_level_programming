#!/usr/bin/python3
"""save_to_json method"""
import json


def save_to_json_file(my_obj, filename):
    """function
        return object to a text file using json

        Args:
                my_obj: object
                filename: file hold object data
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
