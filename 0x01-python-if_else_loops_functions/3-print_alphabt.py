#!/usr/bin/python3
for lowercase in range(97, 123):
    if chr(lowercase) is not 'q' and chr(lowercase) is not 'e':
        print("{}".format(chr(lowercase)), end="")
