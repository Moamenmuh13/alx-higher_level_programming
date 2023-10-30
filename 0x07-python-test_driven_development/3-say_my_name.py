#!/usr/bin/python3
"""
    Print full name.

    Raises:
          TypeError: first_name must be a string or 
                    last_name must be a string

    Args:
        first_name (str): the first name
        last_name (str): the second name. default value empty string

    Returns:
        str : Prints the full name

    """


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    return "My name is {} {}$".format(str(first_name), str(last_name))
