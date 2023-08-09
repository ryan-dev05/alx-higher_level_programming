#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
last_digit = abs(number) & 10
if number < 0:
    last_digit = -last_digit
parity = "even" if last_digit & 2 == 0 else "odd"
print("The string Last digit of"
print(number)
print("the string is")
print(last_digit, "and is", parity)
