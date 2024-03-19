#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
out = 'Last digit of {} is '.format(number)
number_ = abs(number) % 10
sign = None
if number < 0:
    sign = -1
else:
    sign = 1
number_ *= sign
if number_ > 5:
    out += '{} '.format(number_) + 'and is greater than 5'
elif number_ == 0:
    out += '{} '.format(number_) + 'and is 0'
else:
    out += '{} '.format(number_) + 'and is less than 6 and not 0'
print(out)
