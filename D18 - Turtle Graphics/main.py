from turtle import Turtle, Screen

colors = [(210, 234, 244), (18, 112, 172), (187, 16, 63), (232, 144, 74), (243, 218, 77), (171, 44, 105),
          (228, 125, 158), (40, 50, 119), (225, 57, 108), (114, 170, 209), (228, 77, 60), (63, 169, 79),
          (124, 190, 146), (127, 78, 48), (16, 139, 63), (10, 173, 207), (209, 154, 9), (151, 209, 219), (18, 52, 97),
          (23, 96, 47), (117, 43, 35), (252, 228, 0), (69, 76, 41), (5, 78, 51), (240, 163, 186), (153, 210, 195),
          (236, 170, 161)]

turt = Turtle()
turt.speed("fastest")
screen = Screen()
screen.colormode(255)

x = 0
for c in colors:
    turt.color(c)
    turt.begin_fill()
    turt.circle(10)
    turt.end_fill()
    x += 10
    turt.setx(x)

screen.exitonclick()
