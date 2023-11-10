from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

screen.listen()
screen.onkeypress(key="w", fun=lambda: turt.forward(10))
screen.onkeypress(key="Up", fun=lambda: turt.forward(10))
screen.onkeypress(key="s", fun=lambda: turt.backward(10))
screen.onkeypress(key="Down", fun=lambda: turt.backward(10))
screen.onkeypress(key="a", fun=lambda: turt.left(10))
screen.onkeypress(key="Left", fun=lambda: turt.left(10))
screen.onkeypress(key="d", fun=lambda: turt.right(10))
screen.onkeypress(key="Right", fun=lambda: turt.right(10))
screen.onkeypress(key="c", fun=lambda: turt.reset())
screen.onkeypress(key="q", fun=lambda: screen.bye())

screen.exitonclick()
