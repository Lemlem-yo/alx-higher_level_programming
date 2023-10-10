#!/usr/bin/python3
"""write_file method declaration"""


def write_file(filename="", text=""):
    """write_file
                function: user to write the file as you want
       Args:
                filenames: hold the file that written
                text: hold the text that you want to write
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
