#!/usr/bin/python3
"""
takes in a URL,
sends a request to the URL
and displays the body of the response
"""
from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
