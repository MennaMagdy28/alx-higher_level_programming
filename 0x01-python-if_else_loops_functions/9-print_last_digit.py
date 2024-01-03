#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        r = number % 10
    else:
        r = -1 * (number % -10)
    print(r)
    return(r)
