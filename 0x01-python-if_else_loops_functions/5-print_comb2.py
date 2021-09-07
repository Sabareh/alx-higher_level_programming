#!/usr/bin/python3

for digits in range(0, 100):
    if digits == 99:
        print("{}".format(digits))
    else:
        print("{:02}".format(digits), end=", ")
