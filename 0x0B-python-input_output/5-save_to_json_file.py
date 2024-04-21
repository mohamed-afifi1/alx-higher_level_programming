#!/usr/bin/python3
"""
 Module that contains a function that saves an object to a JSON file
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that saves an object to a JSON file """

    with open(filename, 'w') as outfile:
        json.dump(my_obj, outfile)
