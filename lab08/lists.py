#!/usr/bin/env python3

# Nick Stucchi
# 03/30/2017
# main() only executed if the program file is run

def productOfOdd(intList):
    product = 1
    for i in intList:
        if i % 2 != 0:
            product *= i
    return product

def sumOfEven(intList):
    sumEven = 0
    for i in intList:
        if i % 2 == 0:
            sumEven += i
    return sumEven

def evenMembers(intList):
    newIntList = []
    for i in intList:
        if i % 2 == 0:
            newIntList.append(i)
    return newIntList

def changeList(intList):
    for i in range(len(intList)):
        if i % 2 != 0:
            intList[i] = (intList[i] + 1) // 2
        else:
            intList[i] = intList[i] * 3
            
def isReverse(intListOne, intListTwo):
    if intListTwo == intListOne[::-1]:
        return True
    else:
        return False

def main():
    productOfOdd(intList)
    sumOfEven(intList)
    evenMembers(intList)
    changeList(intList)
    isReverse(intListOne, intListTwo)

if __name__ == "__main__":
    main()

