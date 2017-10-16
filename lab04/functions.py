#! /usr/bin/env python3

# Nick Stucchi
# 02/16/2017
# Functions to be used in testsuite.py file

import testsuite

def absolute_value(x):
    if x < 0:
        return -x
    return x

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def to_power(x, y):
    if x ** y:
        return x ** y

def is_greater(x, y):
    if x > y:
        return True
    else:
        return False

def sub_min_max(x, y):
    if x > y:
        return x - y
    else:
        return y - x

def mymax(x, y):
    if x > y:
        return x
    else:
        return y

def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        c = a
        a = b
        b = c + b
    return a
    
def main():
    # use this to test your functions
    pass

if __name__ == '__main__':
    main()
