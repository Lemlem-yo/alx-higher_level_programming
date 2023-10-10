#!/usr/bin/python3
""" append_write method"""


def append_write(filename="", text=""):
    """append to the available file

    Args:
        filename: available file
        text: value that append at the end
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
