#!/usr/bin/python3
"""
 Module that contains a function that converts a json string into a dictionary
"""
import json


def from_json_string(my_str):
    """ Function that converts a JSON string into a dictionary """

    return json.loads(my_str)
