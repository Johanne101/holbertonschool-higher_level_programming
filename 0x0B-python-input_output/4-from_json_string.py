#!/usr/bin/python3
'''Module: from_json_string function'''
import json


def from_json_string(my_str):
    '''returns object (Py D.S.) represented by a JSON string'''
    return json.loads(my_str)
