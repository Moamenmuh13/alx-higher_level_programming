#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds two integers.

    Raises:
          TypeError: If a or b is not an integer or a float.

    Args:
        a (int or float): the first number
        b (int or float): the second number. default value 98

    Returns:
        int : the addition of the a and b

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
