#!/usr/bin/env python3

# Nick Stucchi
# 04/27/2017
# Contains a class named Employee for keeping track of people and their bday

from datetime import date

class Employee:

    def __init__(self, name, sDay, sMonth, sYear):
        self.name = name
        self.sDay = sDay
        self.sMonth = sMonth
        self.sYear = sYear

    def getService(self):
        currentYear = date.today().year
        currentMonth = date.today().month
        if date(self.sYear, self.sMonth, self.sDay) > date.today():
            raise ValueError("Invalid Date")
        else:
            y = currentYear - self.sYear
            m = currentMonth - self.sMonth
            if (m < 0):
                y = y - 1
                m = m + 12
            return str(y) + "-" + str(m)

    def printName(self):
        print(self.name)

    def setName(self, newName):
        self.name = newName

def main():
    emp1 = Employee("Tommy Oliver", 23, 7, 1996)
    emp2 = Employee("Kimberly Hart", 4, 10, 1993)
    emp1.printName()
    print(emp1.getService())
    emp2.printName()
    print(emp2.getService())
    emp1.setName("Billy Cranston")
    emp2.setName("Clark Kent")
    emp1.printName()
    emp2.printName()

if __name__ == '__main__':
    main()

    
        

