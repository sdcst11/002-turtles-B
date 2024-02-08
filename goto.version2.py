import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def square():
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x+20,y)
    t.goto(x+20,y+20)
    t.goto(x,y+20)
    t.goto(x,y)

# Note
# the turtle starts at (0,0).  The coordinates are given as (x,y)
# using the goto(x,y) command does not change the turtle's direction that it is pointing.
t.speed(1)
x = 20
y = 40
square()
x = 50
y = 30
square()
x,y = -30,-10
square()

input()