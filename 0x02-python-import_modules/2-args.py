#!/usr/bin/python3
import sys

if __name__ != '__main__':
    print('exiting !!')
    exit()

arg_str = '{} argument'
argc = len(sys.argv)-1
if argc == 0:
    arg_str += 's.'
elif arg c == 1:
    arg_str += ':'
else:
    arg_str += 's:'
print(arg_str.format(argc))

i = 0
for arg in sys.argv:
    if i != 0:
        print('{:d}: {:s}'.format(i, arg))
    i += 1
