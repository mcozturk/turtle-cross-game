from turtle import Turtle
from random import choice

DEFAULT_Y_CORDS = []
for i in range(-220, 260, choice(range(20, 40, 5))):
    DEFAULT_Y_CORDS.append(i)


class Obstacle:
    def __init__(self):
        self.obstacles = []
        self.create_obstacle()

    def create_obstacle(self):
        for y_cor in DEFAULT_Y_CORDS:
            rand_x = choice(range(-260, 620, 5))
            turtle = Turtle("turtle")
            turtle.penup()
            turtle.goto(rand_x, y_cor)
            turtle.shape("square")
            turtle.color("white")
            turtle.shapesize(stretch_wid=1, stretch_len=2)
            self.obstacles.append(turtle)

    def move(self):
        rand_x = choice(range(320, 800, 5))
        for obstacle in self.obstacles:
            if obstacle.xcor() > -310:
                obstacle.goto(obstacle.xcor() - 10, obstacle.ycor())
            else:
                obstacle.goto(rand_x, obstacle.ycor())

    def refresh(self):
        for obstacle in self.obstacles:
            obstacle.hideturtle()
            obstacle.clear()
        self.obstacles = []
        self.create_obstacle()
