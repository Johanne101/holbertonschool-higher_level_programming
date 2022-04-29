#!/usr/bin/python3
"""
script takes URL,& email,
sends post request
displays body of the response
(decoded in utf-8)
"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf8')  # data changed
    with urllib.request.urlopen(url, data) as response:
        the_page = response.read()
        print(the_page.decode("utf-8"))
