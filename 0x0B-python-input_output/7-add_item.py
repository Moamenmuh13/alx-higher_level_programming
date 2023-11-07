#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""

import sys

if __name__ == "__main__":
    save_to_json_file = __import__
    ("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__
    ("6-load_from_json_file").load_from_json_file

    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    existing_list.extend(sys.argv[1:])
    """Save the updated list to "add_item.json"""
    save_to_json_file(existing_list, "add_item.json")
