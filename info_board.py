from turtle import Turtle
import time


class InfoBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.level = 1
        self.level_info()

    def level_up(self):
        self.level += 1

    def level_info(self):
        self.goto(0, 270)
        self.write(f"Level : {self.level}", align="center", font=('Arial', 15, 'normal'))

    def refresh(self):
        self.clear()
        self.level_info()

    def countdown(self):
        self.clear()
        for second in range(3, 0, -1):
            self.write(f"LEVEL {self.level} STARTING : {second}", align="center", font=('Arial', 20, 'normal'))
            self.clear()
            time.sleep(1)

    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0, 0)
        self.write(f"GAME OVER AT LEVEL {self.level}", align="center", font=('Arial', 30, 'bold'))

