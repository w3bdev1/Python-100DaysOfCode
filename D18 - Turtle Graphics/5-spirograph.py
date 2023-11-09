from turtle import Turtle, Screen
from random import randint, choice

turt = Turtle()
turt.speed("fastest")
screen = Screen()
screen.colormode(255)


def randomize_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turt.pencolor((r, g, b))


def draw_spiro(angular_gap: int):
    for angle in range(0, 360, angular_gap):
        randomize_color()
        turt.setheading(angle)
        turt.circle(100)


draw_spiro(5)

screen.exitonclick()
