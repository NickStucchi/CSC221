#!/usr/bin/env python3
# Nick Stucchi
# 02/23/2017
# Lab05 - Blackout Mathi
from puzzle import *

def checkExpression(exp):
    (left, right) = exp.split("=")
    return eval(left) == eval(right)

def getPuzzleSolution(puz):
    variations = getValidVariations(puz)
    for p in variations:
        if(checkExpression(p)):
            return p

def main():
    n = getPuzzleList()
    for i in n:
        print(getPuzzleSolution(i))
    # Use "getPuzzleList()" function of the puzzle module
    # to get a list of puzzles to solve, then iterate
    # throught that list and print the puzzle's solution
    # with a call to the getPuzzleSolution function you create

if __name__ == '__main__':
    main()
