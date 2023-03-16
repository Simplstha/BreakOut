from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("pink")
        self.shapesize(stretch_wid=1.5, stretch_len=7)
        self.up()
        self.goto(0, -280)

    def move_right(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())