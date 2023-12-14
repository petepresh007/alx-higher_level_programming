#!/usr/bin/python3
""" square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get and set width """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ print a string """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
