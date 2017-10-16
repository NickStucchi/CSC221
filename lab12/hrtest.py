#!/usr/bin/env python3
# Tyler Whitney
# 11/22/2016
# Lab 12 HR System Test

from classes import Employee, Supervisor

def main():
    print("Creating 'Supervisor' object 'tyler'")
    tyler = Supervisor("Tyler Whitney", "09171987", "Computing Systems")
    tyler.printName()
    print("Is Manager? " + str(tyler.isManager()))
    print("Service: " + tyler.getService())

    print('')

    print("Creating 'Employee' object 'one'")
    one = Employee("John Doe", 9, 12, 1982)
    one.printName()
    print("Service Length: " + str(one.getService()))
    
    print('')
    
    print("Added 'one' as employee under 'tyler'")
    tyler.addEmployee(one)
    print("-- Emplyoees under 'tyler' object")
    tyler.printEmployeeNames()
    print(" ----- ")
    print("Is 'tyler' Manager? " + str(tyler.isManager()))

    print('')
 
    print("Creating 'Supervisor' object 'two'")
    two = Supervisor("Eric Twofer", "08231999", "Marketing and Communications")
    two.printName()
    print("Changing name of 'two' to a different name and department")
    two.setName("Eric J Twofer", "MarCom")
    two.printName()
    print("Service Length: " + str(two.getService()))

    print('')

    print("Setting contact info for object 'tyler'")
    tyler.setContactInfo("5642449", "5552400", "whit4763@plattsburgh.edu")
    info = tyler.getContactInfo()
    print("-- Printing Contact Info from 'getContactInfo' method --")
    print("Phone: " + info['phone'])
    print("Fax: " + info['fax'])
    print("Email: " + info['email'])
    print(" ----- ")
    print("-- Printing Contact Info from individual 'getPhone', 'getFax', 'getEmail' methods --")
    print("Phone: " + tyler.getPhone())
    print("Fax: " + tyler.getFax())
    print("Email: " + tyler.getEmail())
    print(" ----- ")

    print('')

    print("Adding 'two' object as employee under 'tyler'")
    tyler.addEmployee(two)
    print("-- Employees under 'tyler' object -- ")
    tyler.printEmployeeNames()
    print(" ----- ")
    print("Removing 'two' object from employee under 'tyler', ('Eric J Twofer')")
    tyler.removeEmployee("Eric J Twofer")
    print("-- Employees under 'tyler' object --")
    tyler.printEmployeeNames()
    print(" ----- ")

if __name__ == "__main__":
    main()
