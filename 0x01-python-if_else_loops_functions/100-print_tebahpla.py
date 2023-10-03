#!/usr/bin/python3
for chars in range(ord('z'), ord('a')-1, -1):
    if chars % 2 == 0:
        diff_char = 0
    else:
        diff_char = 32
    print("{}".format(chr(chars - diff_char)), end="")
