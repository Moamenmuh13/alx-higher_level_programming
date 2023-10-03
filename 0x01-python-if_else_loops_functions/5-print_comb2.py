#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print(f"{number}",'\n', end='')
    else:
        print(f"{number:02d}, ", end='')
