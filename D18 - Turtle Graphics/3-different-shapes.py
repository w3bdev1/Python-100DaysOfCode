from turtle import Turtle, Screen

turt = Turtle()


def draw_polygon(number_of_sides: int):
    internal_angle = 360 / number_of_sides

    for _ in range(number_of_sides):
        turt.fd(100)
        turt.right(internal_angle)


for side in range(3, 11):
    draw_polygon(side)

screen = Screen()
screen.exitonclick()
