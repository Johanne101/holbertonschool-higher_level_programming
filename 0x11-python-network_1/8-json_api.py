#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = {'q': ""}
    else:
        q = {'q': sys.argv[1]}
    response = requests.post('http://0.0.0.0:5000/search_user', data=q)
    try:
        json_response = response.json()
        if json_response == {}:
            print('No result')
        else:
            print("[{}] {}".format(json_response['id'], json_response['name']))
    except ValueError:
        print('Not a valid JSON')
