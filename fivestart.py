from turtle import Turtle

p = Turtle()
p.speed(3)
p.pensize(5)
p.color("black",'yellow')
#p.fillcolor("red")
p.begin_fill()
for i in range(10):
    p.forward(400)
    p.right(144)
p.end_fill()
