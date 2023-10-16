#!/usr/bin/python3
"""base class """


class Base:
    """class define the attributes

        Args:
                nb_objects: a privat class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constractor to assign the private class attrbuite"""

        if id not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
