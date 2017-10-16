#!/usr/bin/env python3

# Nick Stucchi
# 04/13/2017
# puzzle.py to complete blackout.py

def getPuzzleList():
    infile = open("puzzles.txt", 'r')
    puzLine = infile.readlines()
    return puzLine

def getValidVariations(puz):
    newList = []
    c1 = 0
    while c1 < len(puz):
        temp = list(puz)
        if(temp[c1] == "="):
            c1 = c1 + 1
            continue
        del temp[c1]
        c1 = c1 + 1
        while c2 < len(temp):
            temp2 = list(temp)
            if(temp2[c2] == "="):
                c2 = c2 + 1
                continue
            del temp2[c2]
            c2 = c2 + 1
            newExp = ''.join(temp2)
            try:
                left, right = newExp.split("=")
                eval(left)
                eval(right)
            except TypeError:
                continue
            except SyntaxError:
                continue
            newList = newList + [newExp]
    return newList
