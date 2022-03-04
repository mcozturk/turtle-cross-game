from tortoise import Tortoise
from obstacles import Obstacle
from turtle import Screen
from info_board import InfoBoard
import time


def tortoise_crash():
    for obst in obstacle.obstacles:
        if tortoise.distance(obst.xcor() - 25, obst.ycor()) < 20 or tortoise.distance(obst.xcor() + 25, obst.ycor()) < 20:
            return True


screen = Screen()
screen.tracer(0)
info_board = InfoBoard()
screen.title("Turtle Cross Game")
obstacle = Obstacle()
tortoise = Tortoise()


screen.setup(width=600, height=600)
screen.bgcolor("black")

speed = 0.1
should_continue = True
while should_continue:
    if tortoise_crash():
        should_continue = False
    obstacle.move()
    time.sleep(speed)
    screen.update()

    screen.onkeypress(key="w", fun=tortoise.go_up)
    screen.onkeypress(key="s", fun=tortoise.go_down)
    screen.onkeypress(key="a", fun=tortoise.go_left)
    screen.onkeypress(key="d", fun=tortoise.go_right)
    screen.listen()
    if tortoise.passed_finishline():
        info_board.level_up()
        info_board.countdown()
        info_board.refresh()
        if speed > 0.01:
            speed -= 0.01
        elif speed == 0.01:
            speed -= 0.005
        else:
            pass
        obstacle.refresh()
info_board.game_over()
screen.exitonclick()
