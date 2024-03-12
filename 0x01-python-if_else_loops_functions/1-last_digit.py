#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
out = f'Last digit of {number} is '

number_ = number % 10

if number_ > 5:
    out += f'{number_} ' + 'and is greater than 5'
elif  number_ == 0:
    out += f'{number_} ' + 'and is 0'
else:
    out += f'{number_} ' + 'and is less than 6 and not 0'
print(out)
