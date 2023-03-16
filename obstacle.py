from turtle import Turtle
# normal size of a turtle in pixel is 21 x 21


class Obstacles(Turtle):

    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=4)
        self.color(color)
        self.pu()
        self.goto(x, y)
