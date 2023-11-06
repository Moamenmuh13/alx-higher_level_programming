#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """area function that not implemented yet."""

    def area(self):
        raise Exception("area() is not implemented")

    """
    Function to check if the value is valid or not
    Args:
        name (str): The name of the parameter.
        value (int): The parameter to validate.
    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is <= 0.
    """

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
