#!/usr/bin/python3
""" Finds if there's a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """Finds peak in unsorted list of integers"""
    if not list_of_integers:
        return None
    return max(list_of_integers)
