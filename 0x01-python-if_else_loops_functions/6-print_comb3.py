#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        if x < 9:
            print("{:d}{:d}".format(x, y), end="")
        if  x + y != 89:
            print(", ", end="")
        else:
            print("")
