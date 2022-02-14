"""Turtle Tutorial Set Up"""


from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()
leo.color(113, 56, 252)
leo.speed(5)

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i += 1

leo.penup()
leo.goto(-45, -45)
leo.pendown()

leo.begin_fill()
i = 0
while i < 3:
    leo.forward(500)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.goto(0, 50)
bob.speed(25)

bob.penup()
bob.goto(-45, -45)
bob.pendown()
i = 0
while i < 3:
    bob.forward(500)
    bob.left(120)
    i += 1

side_length: int = 300

i: int = 0
while (i < 25):
    bob.forward(side_length)
    bob.left(122)
    i = i + 1

done()