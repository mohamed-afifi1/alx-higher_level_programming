#!/usr/bin/python3
"""This modules Defines a rectangle model class."""
from models.rectangle import Rectangle  # type: ignore


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id=None)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
