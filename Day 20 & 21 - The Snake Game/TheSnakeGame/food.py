from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randon_x = random.randint(-280, 280)
        randon_y = random.randint(-280, 280)
        self.goto(randon_x, randon_y)
