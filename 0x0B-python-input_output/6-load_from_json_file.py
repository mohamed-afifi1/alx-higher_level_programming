#!/usr/bin/python3
"""
 Module that contains a function that loads an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Function that loads an object from a JSON file """

    with open(filename, 'r') as infile:
        return json.load(infile)
