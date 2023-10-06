#!/usr/bin/python3
"""A ALx TDD test for task 2"""


def say_my_name(first_name, last_name=""):
    """Prints full name to screen"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    say_my_name()
