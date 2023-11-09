from turtle import Turtle, Screen
from random import randint, choice

turt = Turtle()
turt.pensize(3)
turt.speed("fastest")
screen = Screen()
screen.colormode(255)
directions = [0, 90, 180, 270]


def randomize_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turt.pencolor((r, g, b))


def random_motion():
    turt.fd(20)
    turt.setheading(choice(directions))


for _ in range(200):
    randomize_color()
    random_motion()

screen.exitonclick()
