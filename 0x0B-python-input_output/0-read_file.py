#!/usr/bin/python3
""" read method declaration """


def read_file(filename=""):
    """ read_file method
                function that reaed text file(UTF-8)

        Args:
                filename: value hold for the file that open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read())
