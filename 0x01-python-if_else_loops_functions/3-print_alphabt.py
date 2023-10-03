#!/usr/bin/python3
for letter in range(ord("a"), ord("z") + 1):
    if letter == ord("e"):
        pass
    elif letter == ord("q"):
        pass
    else:
        print("{:c}".format(letter), end="")
