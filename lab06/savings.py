#!/usr/bin/env python3

# Nick Stucchi
# 03/02/2017
# Calculate how many years to get to target amount.


def main():
    start = eval(input("How much money to start? "))
    apr = eval(input("What is the apr? "))
    target = eval(input("What is the amount you want to get to? "))
    year = 1

    while (1):
        nextYear = start * apr
        start += nextYear
        print("After year " + str(year) + " the account is at ", round(start,2))
        if start >= target:
            break
        year += 1
    
if __name__ == '__main__':
    main()
