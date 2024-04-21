#!/usr/bin/python3
"""
a module that contains a class of student
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

    def to_json(self, attrs=None):
        """
        a function that returns the dictionary description
        """
        if type(attrs) is list:
            dictionary = {}
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__

                if attr in self.__dict__:
                    dictionary[attr] = self.__dict__[attr]
            return dictionary
        else:
            return self.__dict__.copy()
