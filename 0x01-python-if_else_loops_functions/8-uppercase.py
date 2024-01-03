#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) > 96 and ord(a) < 123:
            cnv = 32
        else:
            cnv = 0
        print("{:c}".format(ord(a) - cnv), end='')
    print()
