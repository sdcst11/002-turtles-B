import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# Note
# the turtle starts at (0,0).  The coordinates are given as (x,y)
# using the goto(x,y) command does not change the turtle's direction that it is pointing.
t.penup()
t.speed(1)
t.goto(30,30)
t.pendown()
t.goto(50,30)
t.goto(50,50)
t.goto(30,50)
t.goto(30,30)


input()