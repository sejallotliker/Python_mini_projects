import turtle
turtle.bgcolor("lightpink")
turtle.pensize(2.5)
turtle.speed(0.5)
color=["red","blue","green","orange"]
for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(100) #shape
        turtle.right(10) #direction

turtle.mainloop()
