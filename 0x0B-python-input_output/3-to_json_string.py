#!/usr/bin/python3
import json
""" to_json_string method"""


def to_json_string(my_obj):
    """ function

                the return the JSON representation
        Args:
                my_obj: an object continer
    """
    json_string = json.dumps(my_obj)
    return json_string
