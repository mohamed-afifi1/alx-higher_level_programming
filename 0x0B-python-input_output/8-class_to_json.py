#!/usr/bin/python3
"""
Module containing  a function that returns the dictionary description
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description
    """
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
