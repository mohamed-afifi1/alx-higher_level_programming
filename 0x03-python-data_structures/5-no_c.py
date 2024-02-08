#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)

    new = my_string[:]

    for i in range(length):
        if new[i] == 'c' or new[i] == 'C':
            new = new[:i] + new[i+1:]
    return (new)
