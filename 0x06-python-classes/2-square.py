#!/usr/bin/python3
"""Define a class square"""


class Square:
    """
    This class defines a square by the size attribute.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int) : The size of the sqaure."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
