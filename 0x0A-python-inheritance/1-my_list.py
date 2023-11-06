#!/usr/bin/python3
"""Defines an class that inherited lookup function."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        sortedList = sorted(self)
        """print sorted list"""
        print(sortedList)
