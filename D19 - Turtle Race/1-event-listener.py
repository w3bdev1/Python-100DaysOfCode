from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()


def move_fd():
    turt.fd(10)


screen.listen()
screen.onkey(key="space", fun=move_fd)
screen.exitonclick()
