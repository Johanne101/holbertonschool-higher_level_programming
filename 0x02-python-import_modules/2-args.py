#!/usr/bin/python3


import sys

if __name__ == "__main__":
    """
    1)set value of lengh
        print # arg
    2) print # of listed arg
    3)print Function
    """
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")

    elif argc == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(argc))

    sys.argv.pop(0)
    for index, elmnt in enumerate(sys.argv):
        print("{}: {}".format(index + 1, elmnt))
