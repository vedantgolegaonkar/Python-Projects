from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "purple", "blue"]
STARTING_MOVE_SPEED = 5
INCREMENT_SPEED = 3


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_move_speed = STARTING_MOVE_SPEED

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_move_speed)

    def level_up(self):
        self.car_move_speed += INCREMENT_SPEED
