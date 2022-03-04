from turtle import Turtle


class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color("white", "orange")
        self.setheading(90)
        self.shape("turtle")
        self.start_position = (0, -280)
        self.goto(self.start_position)

    def passed_finishline(self):
        if self.ycor() > 260:
            self.clear()
            self.goto(self.start_position)
            return True
        else:
            pass

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def go_left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def go_right(self):
        self.goto(self.xcor() + 20, self.ycor())
