#!/usr/bin/python3
hello = range(0, 100)

def is_one_digit(number:int) -> str:
    if  number in range(0, 10):
        return f'0{x}'
    else:
        return number

for x in hello:
    if x == hello[-1]:
        print(x)
    else:
        var = is_one_digit(x)
        print(var, end=',')
