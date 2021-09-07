#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number), end=" ")
if ((number % 10) > 5):
    print("{} is greater than 5".format(number % 10))
elif ((number % 10) == 0):
    print("{} and is 0".format(number % 10))
elif ((number % 10) < 6) and ((number % 10) != 0):
    print("{} and is less than 6 and not 0".format(number % 10))
