from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=400)
color =["Red","Blue","Yellow","Purple","Green"]
y_pos = [-60,-30,0,30,60]
is_race_on = False
all_turtles = []

user_bet = (screen.textinput(title="Make Your Bet",
                            prompt="Which Turtle will win the race? Choose your color:\nRed\nBlue\nYellow\nPurple\nGreen").lower())


for turtle_index in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-380,-y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
