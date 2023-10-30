#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
         number_of_instances (int): The number of Rectangle instances.
         print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        tmp_rect = []
        for i in range(self.__height):
            [tmp_rect.append(self.print_symbol) for j in range(self.__width)]
            if i != self.__height - 1:
                tmp_rect.append("\n")
        return "".join(tmp_rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        tmp_rect = "Rectangle(" + str(self.__width)
        tmp_rect += ", " + str(self.__height) + ")"
        return tmp_rect

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
