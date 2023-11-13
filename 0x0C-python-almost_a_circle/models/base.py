#!/usr/bin/python3
""" Define a Base class"""


class Base:
    """Private class attribute to keep track of the number of objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    pass
