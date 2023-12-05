#!/usr/bin/python3
""" write file module """


def write_file(filename="", text=""):
    """ function """

    with open(filename, "w", encoding="utf-8") as f:
        write_file = f.write(text)
        return write_file
