#!/usr/bin/python3


class MyList(list):
    def print_sorted(self):
        sortedList = sorted(self)
        print(sortedList)
