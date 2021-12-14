#!/usr/bin/python3
'''Module: add_arguments function'''


import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
'''script adds all arguments to a Python list, and then save them to a file'''
dlist = []

try:
    dlist = load_from_json_file("add_item.json")
except:
    pass
for i in range(1, len(argv)):
    dlist.append(argv[i])

save_to_json_file(dlist, "add_item.json")
