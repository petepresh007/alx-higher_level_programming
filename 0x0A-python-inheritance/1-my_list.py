#!/usr/bin/python3
""" module for my list class"""


class MyList(list):
    """class extends list"""

    def print_sorted(self):
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
