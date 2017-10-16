#!/usr/bin/env python3
# Nick Stucchi
# 04/06/2017
# Binary Search

# Function to read the names and serials into lists
def getLists():
    infile = open("products.txt",'r')
    line = infile.readline()

    names = []
    numbers = []

    while line != "":
        line = line.strip()
        name, number = line.split(',')
        names = names + [name]
        numbers = numbers + [number]
        line = infile.readline()

    infile.close()
    return names, numbers

# Function to find the name and return the associated phone number
# You must complete this function!
def binarySearch(names, serials, name):
    # left side of list    
    left = 0	
    # right side of the list				
    right = len(names) - 1
    found = False
    while( left <= right and not found):
        mid = (right + left) // 2
        if names[mid] == name:
            found = serials[mid]
            return found
        else:
            if name < names[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return "Not found"

    # -- HINTS -- #
    # Will need a while loop here       
        # find the middle of the list
        # Determine which side of the list to use
        # Return if match found
    # Return "not found" if no match found

# Main Function
def main():
    # Get the lists
    names, serials = getLists()
    # Get the name to search for
    theName = input("Enter the product name to search for: ")

    # Find the phone number for the given name
    serialNum = binarySearch(names, serials, theName)
    print("The product number for ", theName, " is ", serialNum)

if __name__ == "__main__":
    main()
