#!/usr/bin/python3
import hidden_4

counter = 0

if __name__ == '__main__':
    mylist = dir(hidden_4)
    newlist = sorted(mylist)
    while counter < len(newlist):
        if newlist[counter][0] != '_':
            print(newlist[counter])
        counter += 1
