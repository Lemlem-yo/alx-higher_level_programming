#!/usr/bin/python3
"""A ALx module for TDD task 5"""


def text_indentation(text):
    """Prints text with indentation"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    prev = None
    is_indent = 0
    for i in text:
        if i in ['.', '?', ':']:
            print(i, end='\n\n')
            is_indent = 1
        elif i != ' ':
            print(i, end='')
            is_indent = 0
        elif (not is_indent) and i == ' ':
            print(i, end='')
        prev = i
