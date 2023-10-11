#!/usr/bin/python3
""" load_from_json_file methon"""
import json


def load_from_json_file(filename):
    """method that load the json file
        Args:
                filename: file that loaded json file
    """
    with open(filename) as file:
        return json.load(file)
