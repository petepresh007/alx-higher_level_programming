#!/usr/bin/python3
""" reactangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """validation class"""

    def __init__(self, width, height):
        """ validate """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """printing th area"""
        return self.__width * self.__height

    def __str__(self):
        """string rep method"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
