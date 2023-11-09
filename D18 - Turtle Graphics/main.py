import colorgram
from turtle import Turtle, Screen

colors = colorgram.extract("image.jpg", 30)
colors = [tuple(color.rgb) for color in colors]
turt = Turtle()
turt.speed("fastest")
screen = Screen()
screen.colormode(255)

print(colors)

x = 0
for c in colors:
    turt.color(c)
    turt.begin_fill()
    turt.circle(10)
    turt.end_fill()
    x += 10
    turt.setx(x)

screen.exitonclick()
