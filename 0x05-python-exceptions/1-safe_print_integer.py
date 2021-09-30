#!/usr/bin/python3


def safe_print_integer(value):
    try:
        str.format("{:d}", value)
        return (True)
    except ValueError:
        return (False)
