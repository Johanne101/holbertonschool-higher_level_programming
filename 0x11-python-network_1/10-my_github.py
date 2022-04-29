#!/usr/bin/python3
"""Script  that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
import sys

if __name__ == "__main__":
    gitHub_url = 'https://api.github.com/user'
    response = requests.get(gitHub_url, auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get('id'))
