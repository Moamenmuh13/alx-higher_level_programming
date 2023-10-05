#!/usr/bin/python3
from sys import argv
arg_count = len(argv) - 1

if len(argv) == 0:
    print("0 arguments.")
else:
    print("{} arguments{}.".format(arg_count,'s' if arg_count != 1 else ''))

for i in range(1, arg_count + 1):
    print("{}: {}".format(i, argv[i]))
    
if arg_count > 0:
    print()