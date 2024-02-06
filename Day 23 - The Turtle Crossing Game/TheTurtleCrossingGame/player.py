from turtle import Turtle

LOCATION = (0, -280)
MOVE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def up(self):
        self.forward(MOVE)

    def go_to_start(self):
        self.goto(LOCATION)

    def player_is_at_finish_line(self):

        if self.ycor() > 270:
            return True
        else:
            return False
