#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for idx in range(list_length):
        try:
            element = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
            element = 0
        except TypeError:
            print("wrong type")
            element = 0
        except IndexError:
            print("out of range")
            element = 0
        finally:
            newlist.append(element)
    return newlist
