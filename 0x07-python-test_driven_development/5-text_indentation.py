#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after each of
    these characters: `.`, `?` and `:`
    Args:
        text (str): text/str w/ new lines
    Raises:
         TypeError: text must be a string"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = ".?:"
    break_txt = text.strip()

    for nstr in break_txt:
        if nstr not in flag:
            print(nstr, end="")
        else:
            print(nstr + "\n\n")
    print()
