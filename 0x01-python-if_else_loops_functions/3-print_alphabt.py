#!/usr/bin/python3

for x in range(ord('a'), ord('z') + 1):
    if chr(x) in ['q', 'e']:
        pass
    else:
        print(x, end='')
