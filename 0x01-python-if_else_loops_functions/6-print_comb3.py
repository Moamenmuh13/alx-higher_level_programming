#!/usr/bin/python3
for first_num in range(0, 10):
    for sec_num in range(first_num + 1, 10):
        if first_num == 8 and sec_num == 9:
            print('89')
        else:
            print('{}{}, '.format(first_num, sec_num), end='')
