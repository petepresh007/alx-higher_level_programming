#!/usr/bin/python3
""" Append Module"""


def append_write(filename="", text=""):
    """ append function
        args:
        filename: the name of the file
        text: the message to append
    """

    with open(filename, "a", encoding="utf-8") as f:
        append_f = f.write(text)
        return append_f
