#prompt the user to enter values
import turtle
x1,y1 = eval(input("enter the center of circle x1,y1: "))
radius = eval(input("enter the value of the radius: "))
x2,y2 = eval(input("enter a point x2,y2: "))
#draw the circle
turtle.penup()
turtle.goto(x1, y1-radius)
turtle.pendown()
turtle.circle(radius)
#draw the point
turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.begin_fill()#begin to fill the color in a shape
turtle.color("red")
turtle.circle(3)
turtle.end_fill()
#Display the status
turtle.penup()
turtle.goto(x1-70, y1-radius-20)
turtle.pendown()
d = ((x2-x1) *(x2-x1) + (y2-y1)*(y2-y1) ** 0.5)
if d <= radius:
    turtle.write("The point is inside the circle")
else:
    turtle.write("The point is outside the circle")
turtle.hideturtle()
turtle.done()
