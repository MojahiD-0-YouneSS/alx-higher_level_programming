#!/usr/bin/python3

alphabit = range(ord('a'), ord('z') + 1)

for x in alphabit:
    if chr(x) in ['q', 'e']:
        pass
    else:
        print(x, end='')
