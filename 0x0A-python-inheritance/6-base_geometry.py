#!/usr/bin/python3
""" geometry module """


class BaseGeometry(object):
    """ raises an exception """

    def area(self):
        raise Exception("area() is not implemented")
