#!/usr/bin/python3
if __name__ == "__main__":
    """ "Print the number of list of arguments"""
import sys

arg_count = len(sys.argv) - 1

if len(sys.argv) == 0:
    print("0 arguments.")
else:
    print("{} arguments{}.".format(arg_count, "s" if arg_count != 1 else ""))

for i in range(1, arg_count + 1):
    print("{}: {}".format(i, sys.argv[i]))

if arg_count > 0:
    print()
