from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.pu()
        self.a = 10
        self.b = 10
        self.pace = 0.1

    def move(self):
        x = self.xcor() + self.a
        y = self.ycor() + self.b
        self.goto(x, y)

    def bounce_y(self):
        self.b *= -1

    def bounce_x(self):
        self.a *= -1
        self.pace *= 0.8

    def reset(self):
        self.goto(0, 0)
        self.bounce_y()
        self.pace = 0.1

