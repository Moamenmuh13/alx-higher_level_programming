#!/usr/bin/python3
""" Define a write a text in file function"""


def write_file(filename="", text=""):
    """Return the length of the text"""
    with open(filename, "w", encoding="utf-8") as file:
        character = file.write(text)

    return character
