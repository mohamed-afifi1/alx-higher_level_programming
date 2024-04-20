#!/usr/bin/python3
""" Module that contains a function that writes to a file """


def write_file(filename="", text=""):
    """ Function that writes to a file """

    with open(filename, "w") as f:
        f.write(text)
