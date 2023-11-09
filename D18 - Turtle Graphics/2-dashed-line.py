from turtle import Turtle, Screen

turt = Turtle()

for _ in range(10):
    turt.fd(10)
    turt.penup()
    turt.fd(10)
    turt.pendown()

screen = Screen()
screen.exitonclick()
