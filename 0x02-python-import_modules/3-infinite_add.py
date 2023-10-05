#!/usr/bin/python3
if __name__ == "__main__":
    """Print the additin of all arguments"""
import sys

arg_count = len(sys.argv) - 1

if arg_count == 0 or arg_count == 1:
    print("0")
else:
    total = 0

for i in range(arg_count):
    total = total + int(sys.argv[i + 1])
    
print("{}".format(total))
