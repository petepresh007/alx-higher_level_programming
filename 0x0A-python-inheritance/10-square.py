#!/usr/bin/python3
""" square module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ the square class """
    def __init__(self, size):
        """ size constructor """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ square the area """
        return self.__size ** 2
