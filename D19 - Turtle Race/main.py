from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
PADDING = 20
INITIAL_X = -(screen.window_width() / 2) + PADDING

colors = ["violet", "blue", "green", "yellow", "orange", "red"]
user_bet = screen.textinput(title="Make your bet",
                            prompt=f"Which turtle will win the race? ({'/'.join(c for c in colors)}) ").lower()
turtles = []
y = -125

for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=INITIAL_X, y=y)
    turtles.append(t)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > (250 - 20):
            is_race_on = False
            winner_color = turtle.pencolor()
            print(f"{winner_color.title()} turtle is the winner!")
            turtle.goto(0, 0)
            if winner_color == user_bet:
                turtle.write("I'm the winner.\nYou've won!", True, "center", ("monospace", 12, "normal"))
            else:
                turtle.write("I'm the winner.\nYou've lost!", True, "center", ("monospace", 12, "normal"))
        else:
            random_distance = randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
