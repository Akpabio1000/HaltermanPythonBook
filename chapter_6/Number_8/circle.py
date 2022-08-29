'''
Solution to pythonbookHalterman.
Chapter 6, no. 8.

Last updated: 29/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''
import turtle

radius = 100 

turtle.pencolor('blue')
turtle.tracer(0)

turtle.penup()
turtle.setposition(0, -radius)   #positions circle at centre of window
turtle.pendown()

turtle.circle(radius)

turtle.hideturtle()
turtle.update()
turtle.done()
                        
                        
