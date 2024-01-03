#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if int(a) > 96 and int(a) < 123:
            cnv = 32
        else:
            cnv = 0
        print("{:c}".format(a - cnv), end='')
    print()
