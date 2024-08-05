#!/usr/bin/python3
"""
find peak
"""


def find_peak(list_of_integers):
    """
    Find the peak in a list of integers.
    """
    # Check if the list is empty
    if not list_of_integers:
        return None

    if len(set(list_of_integers)) == 1:
        return list_of_integers[0]

    left = 0
    right = len(list_of_integers) - 1

    while left <= right:
        mid = int((left + right) / 2)

        if list_of_integers[mid] > list_of_integers[mid - 1]\
                and mid == len(list_of_integers) - 1:
            return list_of_integers[mid]
        elif (list_of_integers[mid] > list_of_integers[mid + 1]
                and list_of_integers[mid] > list_of_integers[mid - 1]):
            return list_of_integers[mid]
        elif mid == 0 and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
