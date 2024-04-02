#!/usr/bin/python3
def replace_in_list(my_list, indx, element):
    if indx >= len(my_list) or indx < 0:
        return my_list
    my_list[indx] = element
    return my_list
