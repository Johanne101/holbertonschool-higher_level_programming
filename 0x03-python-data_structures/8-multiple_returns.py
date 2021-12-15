#!/usr/bin/python3


def multiple_returns(sentence):
    """Function returns a tuple w/ length of string &
    its first character."""
    str_lnth = len(sentence)
    return (str_lnth, sentence[0] if str_lnth > 0 else None)
