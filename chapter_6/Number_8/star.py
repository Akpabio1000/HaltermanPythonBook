'''
Solution to pythonbookHalterman.
Chapter 6, no. 8.

Last updated: 27/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''
import turtle

line = 300 #length of line, can be any value of choice

#To determine the amonut of turn,
#Each angle in the pentagon is 108. Hint --> [(2n-4)*90]
#Base angle of isoceles triangle = (180 - 108)/2 = 36
#angle of turn = 180 - 36 = 144

angle = 144

turtle.penup()
turtle.setposition(-100, 0)
turtle.pencolor('red')
turtle.pendown()
turtle.tracer(0)

for i in range(5):
    turtle.forward(line)
    turtle.right(angle)

turtle.hideturtle()
turtle.update()
turtle.done()
                        
                        
