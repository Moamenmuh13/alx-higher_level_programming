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

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""

        if self.size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
