#!/usr/bin/python3
"""

"""


class Student():
    """
    a class that represents a student
    """
    def __init__(self, first_name, last_name, age):
        """
        a function that initializes the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        a function that returns the dictionary description
        """
        return self.__dict__.copy()
