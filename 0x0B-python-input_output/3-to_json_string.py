#!/usr/bin/python3
'''module contains to_json_string function'''
import json


def to_json_string(my_obj):
    '''Function returns JSON representation of an object (string)'''
    return json.dumps(my_obj)
