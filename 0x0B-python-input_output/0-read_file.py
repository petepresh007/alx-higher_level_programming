#!/usr/bin/python3
"""aa function to read a file"""


def read_file(filename=""):
    """ File """

    with open(filename, "r", encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")
