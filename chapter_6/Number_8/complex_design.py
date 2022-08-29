'''
Solution to pythonbookHalterman.
Chapter 6, no. 8.

Last updated: 29/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''
import turtle

radius = 100    # Set radius of circle

angle = 0       # Set angle of radial lines. Initially, first radial line is
                # at zero degrees, increases uniformly anticlockwise.

squares = int(input('How many squares? ')) # Accept number of squares from user

turtle.pencolor('blue')
turtle.tracer(0)
turtle.penup()
turtle.setposition(0, -radius)   #positions circle at centre of window
turtle.pendown()

turtle.circle(radius)           # Draws circle

for i in range(1, squares + 1):
    # draw two radial lines in the circle at 'angle' degrees
    for j in range(2):
        turtle.penup()
        turtle.setposition(0, 0)
        turtle.pendown()
        turtle.forward(radius)
        turtle.setheading(180 + angle)

    # Draw a square for each pair of radial lines drawn
    # The square is drawn from the turtle's last position
    turtle.right(90)
    turtle.forward(radius)
    for k in range(3):
        turtle.right(90)
        turtle.forward(radius * 2)
    turtle.right(90)
    turtle.forward(radius)

    angle = 360/(squares * 2) * i  # Increases 'angle' anticlockwisely
    turtle.setheading(angle)

turtle.hideturtle()
turtle.update()
turtle.done()
                        
                        
