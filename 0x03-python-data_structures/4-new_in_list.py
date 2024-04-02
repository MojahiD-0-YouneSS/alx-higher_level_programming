#!/usr/bin/python3
def new_in_list(my_list, indx, element):
    if indx >= len(my_list) or indx < 0:
        return my_list
    new_list = my_list[:]
    new_list[indx] = element
    return new_list
