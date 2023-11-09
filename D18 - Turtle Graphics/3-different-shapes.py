from turtle import Turtle, Screen
from random import randint

turt = Turtle()
turt.pensize(5)
screen = Screen()


def draw_polygon(number_of_sides: int):
    internal_angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        randomize_color()
        turt.fd(100)
        turt.right(internal_angle)


def randomize_color():
    screen.colormode(255)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turt.pencolor((r, g, b))


for side in range(3, 11):
    draw_polygon(side)

screen.exitonclick()
