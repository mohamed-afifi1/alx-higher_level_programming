#!/usr/bin/python3
""" Module that contains a function that converts an object to a json string"""
import json


def to_json_string(my_obj):
    """ Function that converts an object to a JSON string """

    return json.dumps(my_obj)
