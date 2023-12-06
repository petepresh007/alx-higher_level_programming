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

    def __str__(self):
        '''Returns string representation of this square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
