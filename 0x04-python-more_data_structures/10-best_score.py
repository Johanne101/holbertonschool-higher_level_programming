#!/usr/bin/python3
"""
Method: Returns a key with the biggest integer value (big_k).
"""


def best_score(a_dictionary):
    """
    Assum:
    - all values are only integers.
    - all students have a different score.
    """
    '''
    if a_dictionary:
        dlist = list(a_dictionary)
        big_k = dlist[0]
        for key_item in dlist:
    '''
    '''
    if no score found:
        return None
    '''
    '''
    a_dictionary.sorty()
    return a_dictionary[-1]
        else:
            return None
    '''
    if a_dictionary:
        dscore = max(a_dictionary, key=a_dictionary.get)
        return dscore
    else:
        return None
