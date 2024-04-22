#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base  # type: ignore


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x-coordinate of the new Rectangle.
            y (int): The y-coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @property
    def x(self):
        """Return the x-coordinate of the rectangle."""
        return self.__x

    @property
    def y(self):
        """Return the y-coordinate of the rectangle."""
        return self.__y

    @width.setter
    def width(self, width):
        """Set the width of the rectangle."""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Set the height of the rectangle."""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Set the x-coordinate of the rectangle."""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Set the y-coordinate of the rectangle."""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle."""
        for Y in range(self.y):
            print("")

        for X in range(self.height):
            print(" "*self.x, end="")
            print("#"*self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)
