#!/usr/bin/python3
hello = range(0, 99)
for x in hello:
    print('{:02d}'.format(x), end=', ')
print('{:02d}'.format(x+1), end=' ')
