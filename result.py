from turtle import Turtle

class Result(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("pink")
        self.goto(-200, 0)

    def game_over(self):
        self.write("Game Over!", font=("Courier", 60, "bold"))

    def you_won(self):
        self.write("You Won!!!", font=("Courier", 60, "bold"))