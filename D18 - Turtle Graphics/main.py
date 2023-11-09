from turtle import Turtle, Screen
from random import choice

GAP = 50
POS_X_START = 0
POS_X = 0
POS_Y = 0
colors = [(210, 234, 244), (18, 112, 172), (187, 16, 63), (232, 144, 74), (243, 218, 77), (171, 44, 105),
          (228, 125, 158), (40, 50, 119), (225, 57, 108), (114, 170, 209), (228, 77, 60), (63, 169, 79),
          (124, 190, 146), (127, 78, 48), (16, 139, 63), (10, 173, 207), (209, 154, 9), (151, 209, 219), (18, 52, 97),
          (23, 96, 47), (117, 43, 35), (252, 228, 0), (69, 76, 41), (5, 78, 51), (240, 163, 186), (153, 210, 195),
          (236, 170, 161)]

turt = Turtle()
turt.speed("fastest")
turt.penup()
turt.hideturtle()
screen = Screen()
screen.colormode(255)


def shift_starting_point(number_of_row, number_of_column):
    centre_x = GAP * (number_of_column - 1) / 2
    centre_y = GAP * (number_of_row - 1) / 2
    global POS_X_START, POS_X, POS_Y
    POS_X_START = -centre_x
    POS_X = -centre_x
    POS_Y = -centre_y
    turt.goto(POS_X, POS_Y)


def draw_row(number_of_column):
    for _ in range(number_of_column):
        turt.dot(20, choice(colors))
        global POS_X
        POS_X += GAP
        turt.setx(POS_X)


def draw_matrix(number_of_row, number_of_column):
    shift_starting_point(number_of_row, number_of_column)
    for _ in range(number_of_row):
        draw_row(number_of_column)
        global POS_X, POS_Y
        POS_X = POS_X_START
        turt.setx(POS_X)
        POS_Y += GAP
        turt.sety(POS_Y)


draw_matrix(10, 10)

screen.exitonclick()
