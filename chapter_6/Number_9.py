'''
Solution to pythonbookHalterman.
Chapter 6, no. 9.

Last updated: 29/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''
import turtle
import math

radius = 10    # Set length of side of hexagon 
steps = 6      # Number of sides of polygon

x, y = -250, 210  # set (x, y) coordinates for centre of
                  # first hexagon at the top left corner

turtle.pencolor('blue')
turtle.tracer(0)

for i in range(16): # 16 rows of identical pattern
    for j in range(30): # 30 columns of identical pattern
        turtle.penup()
        turtle.setposition(x, y)   
        turtle.pendown()
        turtle.circle(radius, steps = steps)
        x += radius * math.sqrt(3)  # calculated distance between centres of
                                    # and two hexagons as a function of radius

    x = -250
    for k in range(30):
        turtle.penup()
        turtle.setposition(x, y)
        turtle.setheading(-90)
        turtle.pendown()
        turtle.forward(radius)
        x += radius * math.sqrt(3)

    turtle.setheading(0) #restore turtle heading to default
    x = -250            #set x coordinate to draw next row pattern
    y -= (radius * 3)   #set y coordinate to draw next row pattern
    
turtle.hideturtle()
turtle.update()
turtle.done()
                        
                        
