#!/usr/bin/python3
""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """ Function that reads from a file """

    with open(filename, "r") as f:
        r = f.read()
        print(r, end="")
