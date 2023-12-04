#!/usr/bin/python3
"""class module"""


def inherits_from(obj, a_class):
    """class"""

    return isinstance(obj, a_class) and type(obj) != a_class
