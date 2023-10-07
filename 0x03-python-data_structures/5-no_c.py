#!/usr/bin/python3


def no_c(my_string):
    filtered_string = ""
    for letter in my_string:
        if letter != "c" and letter != "C":
            filtered_string += letter
    return filtered_string
