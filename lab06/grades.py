#!/usr/bin/env python3

# Nick Stucchi
# 03/02/2017
# Calculate average letter grade.

grades = [
    ("Calculus", [100, 95, 90, 92, 100, 100]),
    ("EarthScience", [100, 50, 55, 0, 35, 85]),
    ("PhysicalEd", [100, 100, 100, 95, 98, 92]),
    ("CompSci", [100, 100, 100, 100, 92, 90]),
    ("Accounting", [90, 90, 90, 92, 85, 100])]

def getLetter(num):
    if(num < 65):
        return "F"
    elif(num < 75):
        return "D"
    elif(num < 85):
        return "C"
    elif(num < 95):
        return "B"
    else:
        return "A"
        
def main():
    for (a,b) in grades:
        average = sum(b) / len(b)
        print(a + " \t" + str(round(average,2)) + " \t" + getLetter(average))

if __name__ == "__main__":
    main() 
