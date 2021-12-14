#!/usr/bin/python3
'''Module: load_from_json_file function'''
import json


def load_from_json_file(filename):
    '''Function creates object from a JSON file'''
    with open(filename) as f:
        return json.load(f)
