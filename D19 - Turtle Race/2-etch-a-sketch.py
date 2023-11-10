from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=lambda: turt.forward(10))
screen.onkey(key="s", fun=lambda: turt.backward(10))
screen.onkey(key="a", fun=lambda: turt.setheading(turt.heading() + 10))
screen.onkey(key="d", fun=lambda: turt.setheading(turt.heading() - 10))
screen.onkey(key="c", fun=lambda: turt.reset())
screen.onkey(key="q", fun=lambda: screen.bye())

screen.exitonclick()
