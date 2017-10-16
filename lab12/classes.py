#!/usr/bin/env python3

# Nick Stucchi
# 05/04/2016
# Classes Test

from datetime import date

class Employee:

    def __init__(self, fullName, sDay, sMonth, sYear):
        self.fullName = fullName
        self.sDay = sDay
        self.sMonth = sMonth
        self.sYear = sYear

    def getService(self):
        currentYear = date.today().year
        currentMonth = date.today().month
        today = date.today()
        if (date(int(self.sYear), int(self.sMonth), int(self.sDay)) < today):
            y = currentYear - self.sYear
            m = currentMonth - self.sMonth
            if (m < 0):
                y = y - 1
                m = m + 12
            return str(y) + "-" + str(m)
        else:
            raise ValueError("Invalid Date")

    def printName(self):
        print(self.fullName)

    def setName(self, newName):
        self.fullName = newName

    def getName(self):
        return self.fullName

class Supervisor(Employee):

    def __init__(self, name, startDate, dept):
        Employee.__init__(self, name, int(startDate[2:4]), int(startDate[0:2]), int(startDate[4:9]))
        self.dept = dept
        self.employees = {}
        self.contact_info = {}

    def printName(self):
        print("%s, %s" % (self.fullName, self.dept))

    def setName(self, nName, nDept):
        self.fullName = nName
        self.dept = nDept

    def addEmployee(self, emp):
        self.employees[emp.getName()] = emp

    def isManager(self):
        if len(self.employees) >= 1:
            return True
        else:
            return False
    
    def printEmployeeNames(self):
        for akey in self.employees.keys():
            print(akey)

    def removeEmployee(self, removeName):
        try:
            del self.employees[removeName]
        except:
            pass

    def getContactInfo(self):
        return self.contact_info

    def setContactInfo(self, phone, fax, email):
        self.contact_info["phone"] = phone
        self.contact_info["fax"] = fax
        self.contact_info["email"] = email

    def getPhone(self):
        return self.contact_info["phone"]

    def getFax(self):
        return self.contact_info["fax"]

    def getEmail(self):
        return self.contact_info["email"]































    


