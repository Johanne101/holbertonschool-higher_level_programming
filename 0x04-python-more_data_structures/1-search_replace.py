#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda idx: replace if idx == search else idx, my_list))
