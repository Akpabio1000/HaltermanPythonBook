'''
Solution to pythonbookHalterman.
Chapter 6, no. 8.

Last updated: 27/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''
import turtle

line = 100 #length of line, can be any value of choice
angle = 75 #angle of turn, can be any value of choice

turtle.penup()
turtle.setposition(-100, 0)
turtle.pencolor('red')
turtle.pendown()
turtle.setheading(angle)
turtle.tracer(0)

for i in range(5):
    for j in range(2):
        turtle.forward(line)
        turtle.right(2*angle)
    turtle.setheading(angle)

turtle.hideturtle()
turtle.update()
turtle.done()
                        
                        
