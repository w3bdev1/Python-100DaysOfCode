from turtle import Turtle, Screen

turt = Turtle()


def forward_and_turn_right():
    turt.fd(100)
    turt.rt(90)


for _ in range(4):
    forward_and_turn_right()

screen = Screen()
screen.exitonclick()
