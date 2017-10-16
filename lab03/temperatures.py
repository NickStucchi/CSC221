#!/usr/bin/env python3

# Nick Stucchi
# 02/09/2017
# Program using Turtle Graphics, a for loop, and if statements to create a graph of 25 random temperatures.

import turtle
import random
w = turtle.Screen()
t = turtle.Turtle()
startTemp = random.randrange(20, 100)
for i in range(25):
    temp = random.randrange(20, 100)
    print(temp)
    if temp > startTemp:
        t.color("red")
        t.shape("turtle")
        t.forward(10)
        t.left(90)
        t.forward(temp - startTemp)
        t.right(90)
    else:
        t.color("blue")
        t.shape("turtle")
        t.forward(10)
        t.left(90)
        t.forward(temp - startTemp)
        t.right(90)
    startTemp = temp
print("Thank you, your graph has been created!")

w.mainloop()



    

