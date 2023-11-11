from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
PADDING = 20
INITIAL_X = -(screen.window_width() / 2) + PADDING
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")
print(user_bet)

colors = ["violet", "blue", "green", "yellow", "orange", "red"]
y = -125

for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=INITIAL_X, y=y)
    y += 50

screen.exitonclick()
