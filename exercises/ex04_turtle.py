"""A House My 9-Year-Old Self Would Love.

Creating a function to draw a rectangle (lines 10-24)
Creating a function to draw a triangle (lines 29-43)
Creating a function to draw a line (lines 46-55)
Creating a function to draw a cat toy and call within the cat function (lines 60-72)
Changing the pen size referencing the Turtle documentation page (lines 85 and 93)
Using a loop to create an interesting pattern to draw the cat toy (lines 70-73)
"""

from turtle import Turtle, colormode, done
colormode(255)

author = 730460994


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a rectangle of the given width and length whose top-left corner is located at x, y."""
    a_turtle.speed(0)
    a_turtle.color(0, 0, 0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 2:
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.forward(length)
        a_turtle.right(90)
        i = i + 1


def draw_triangle(a_turtle: Turtle, x: float, y: float, side: float) -> None:
    """Draw a triangle of the given side length whose top-left corner is located at x, y."""
    a_turtle.speed(0)
    a_turtle.color(229, 54, 255)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.begin_fill()
    i: int = 0
    while i < 3:
        a_turtle.forward(side)
        a_turtle.left(120)
        i = i + 1
    a_turtle.end_fill()


def draw_line(a_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draw a line of given length starting at (x, y)."""
    a_turtle.speed(0)
    a_turtle.penup
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.forward(length)


def cat_toy(a_turtle: Turtle, x: float, y: float, side_length: float) -> None:
    """Draw a cat toy whose top-left corner is located at x, y."""
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pencolor(255, 142, 54)
    a_turtle.pendown()
    i: int = 0
    while (i < 100):
        a_turtle.forward(side_length)
        a_turtle.left(122)
        i = i + 1


def cat(a_turtle: Turtle, x: float, y: float) -> None: 
    """Draw a gigantic cat whose top-left corner is located at x, y because my 9-year-old self would love a cat."""
    a_turtle.speed(0)
    a_turtle.color(229, 54, 255)
    draw_rectangle(a_turtle, 100, 50, 100, 40)
    draw_rectangle(a_turtle, 70, 50, 30, 30)

    draw_rectangle(a_turtle, 100, 10, 10, 30)
    draw_rectangle(a_turtle, 120, 10, 10, 30)
    draw_rectangle(a_turtle, 190, 10, 10, 30)
    draw_rectangle(a_turtle, 170, 10, 10, 30)

    draw_rectangle(a_turtle, 80, 40, 3, 3)
    draw_rectangle(a_turtle, 90, 40, 3, 3)

    draw_rectangle(a_turtle, 200, 50, 50, 10)
    
    cat_toy(a_turtle, 60, -10, 20)


def frame(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw the frame of the house."""
    a_turtle.speed(0)
    a_turtle.pensize(4)
    draw_rectangle(a_turtle, -350, 150, 300, 300)
    draw_triangle(a_turtle, -350, 150, 300)
    draw_rectangle(a_turtle, -50, 90, 100, 100)
    draw_rectangle(a_turtle, -30, 50, 40, 60)
    a_turtle.pensize(1)


def ladder(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw the stairs leading up to the house."""
    a_turtle.speed(0)
    draw_rectangle(a_turtle, 0, -10, 20, 20)
    draw_rectangle(a_turtle, 0, -30, 20, 20)
    draw_rectangle(a_turtle, 0, -50, 20, 20)
    draw_rectangle(a_turtle, 0, -70, 20, 20)
    draw_rectangle(a_turtle, 0, -90, 20, 20)
    draw_rectangle(a_turtle, 0, -110, 20, 20)
    draw_rectangle(a_turtle, 0, -130, 20, 20)
    draw_rectangle(a_turtle, 0, -150, 20, 20)


def window(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a window whose top-left corner is located at x, y."""
    draw_rectangle(a_turtle, -300, 125, 30, 50)
    draw_line(a_turtle, -300, 100, 30)
    draw_rectangle(a_turtle, -150, 125, 30, 50)
    draw_line(a_turtle, -150, 100, 30)
    draw_rectangle(a_turtle, -225, 125, 30, 50)
    draw_line(a_turtle, -225, 100, 30)

    draw_rectangle(a_turtle, -300, 50, 30, 50)
    draw_line(a_turtle, -300, 25, 30)
    draw_rectangle(a_turtle, -150, 50, 30, 50)
    draw_line(a_turtle, -150, 25, 30)
    draw_rectangle(a_turtle, -225, 50, 30, 50)
    draw_line(a_turtle, -225, 25, 30)

    draw_rectangle(a_turtle, -300, -25, 30, 50)
    draw_line(a_turtle, -300, -50, 30)
    draw_rectangle(a_turtle, -150, -25, 30, 50)
    draw_line(a_turtle, -150, -50, 30)
    draw_rectangle(a_turtle, -225, -25, 30, 50)
    draw_line(a_turtle, -225, -50, 30)


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    ertle.speed(0)
    frame(ertle, 0, 0)
    window(ertle, 0, 0)
    ladder(ertle, 0, 0)
    cat(ertle, 0, 0)


if __name__ == "__main__":
    main()

done()
