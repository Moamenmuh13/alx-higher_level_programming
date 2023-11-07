#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object as JSON to a text file.

    Args:
        my_obj (Any): The Python object to be serialized to JSON.
        filename (str): The name of the file to save the JSON representation to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
