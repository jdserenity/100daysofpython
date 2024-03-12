from turtle import Turtle
import random
import math
from car import Car
STARTING_MOVE_DISTANCE = 4
MOVE_INCREMENT = 1


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.start_cars()

    def start_cars(self):
        for _ in range(10):
            car = Car()
            rand_x = random.randint(-300, 300)
            rand_y = random.randint(-240, 245)
            car.goto(x=rand_x, y=rand_y)
            self.cars.append(car)

    def gen_car(self, num_cars_to_gen):
        for _ in range(math.floor(num_cars_to_gen)):
            car = Car()
            rand_y = random.randint(-240, 245)
            car.goto(x=320, y=rand_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            x = car.xcor() - self.move_distance
            y = car.ycor()
            car.goto(x, y)

    def increase_move_distance(self):
        self.move_distance += MOVE_INCREMENT
