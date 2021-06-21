from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(f'{random.choice(COLORS)}')
        new_car.shapesize(stretch_wid=2, stretch_len=1)
        new_car.setheading(90)
        self.cars.append(new_car)
