#!/usr/bin/python3
"""student to JSON"""


class Student:
    """class of student"""
    def __init__(self, first_name, last_name, age):
        """init value holder"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get a dictionary"""
        return self.__dict__
