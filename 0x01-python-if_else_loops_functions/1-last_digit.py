#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_num_str = num_str[-1]
last_digit = int(last_num_str)
if last_digit > 5:
    x = "is greater than 5"
elif last_digit == 0:
    x = "and is 0"
elif (last_digit != 0) and (last_digit < 6):
    x = "and is less than 6 and not 0"
        print(f"Last digit of {number} is {last_digit} {x}")
