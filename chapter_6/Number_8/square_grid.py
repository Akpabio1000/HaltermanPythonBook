'''
Solution to pythonbookHalterman.
Chapter 6, no. 8.

Last updated: 27/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''
import turtle

line = 300 #length of line, can be any value of choice
x = -100
y = -100

turtle.pencolor('purple')
turtle.tracer(0)

for i in range(6):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.forward(line)
    y += line/5

turtle.setheading(90)
for i in range(6):
    turtle.penup()
    turtle.setposition(x, -100)
    turtle.pendown()
    turtle.forward(line)
    x += line/5

    

turtle.hideturtle()
turtle.update()
turtle.done()
                        
                        
