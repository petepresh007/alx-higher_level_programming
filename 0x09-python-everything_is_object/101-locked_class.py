#!/usr/bin/python3
"""defining a locked class"""


class LockedClass:
    """prevent the users
    from instattiating the
    class"""
    __slots__ = ("first_name",)
