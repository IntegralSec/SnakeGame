from turtle import Turtle
import random

class Food(Turtle):
    min_x = -280
    max_x = 280
    min_y = -280
    max_y = 280

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.random_move()

    def set_screen_size(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def random_move(self):
        random_x = random.randint(self.min_x, self.max_x)
        random_y = random.randint(self.min_y, self.max_y)
        self.goto(random_x, random_y)
