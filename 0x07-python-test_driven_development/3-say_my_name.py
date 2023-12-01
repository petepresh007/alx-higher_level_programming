#!/usr/bin/python3
""" Printing a string """


def say_my_name(first_name, last_name=""):
    """
    A function to print my name

    Args:
        first_name(str): first name
        last_name(str, optionale): last name

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/3-say_my_name.txt")
