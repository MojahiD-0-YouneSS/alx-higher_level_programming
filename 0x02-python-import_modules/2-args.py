#!/usr/bin/python3
import sys

if __name__ != '__main__':
    print('exiting !!')
    exit()

argstr = '{} argument'
argc = len(sys.argv)-1
if argc == 0:
    argstr += 's.'
elif arg c == 1:
    argstr += ':'
else:
    argstr += 's:'
print(arg_str.format(argc))

i = 0
for arg in sys.argv:
    if i != 0:
        print('{:d}: {:s}'.format(i, arg))
    i += 1
