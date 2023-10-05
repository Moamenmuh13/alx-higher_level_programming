#!/usr/bin/python3
if __name__ == "__main__":
    """ "Print the additin of all arguments"""
    import sys

    total = 0
    for i in sys.argv[1:]:
        total = total + int(i)
        
    print("{:d}".format(total))
