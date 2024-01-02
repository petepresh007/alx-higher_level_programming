#!/usr/bin/python3
"""module for inserting a line"""


def append_after(filename="", search_string="", new_string=""):
    """function to insert a new line"""

    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
