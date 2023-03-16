from turtle import Screen
from result import Result
from obstacle import Obstacles
from ball import Ball
from paddle import Paddle
import time

X_POS = [-360, -270, -180, -90, 0, 90, 180, 270, 360]
Y_POS = [230, 195, 160, 125, 90]
obstacles = []
game_on = True
life = 0

screen = Screen()
screen.title("Break Out!")
screen.screensize(canvwidth=600, canvheight=400, bg="black")
screen.tracer(0)
paddle = Paddle()
ball = Ball()
result = Result()
for pos in X_POS:
    obs = Obstacles(pos, 230, "red")
    obstacles.append(obs)
for pos in X_POS:
    obs = Obstacles(pos, 195, "orange")
    obstacles.append(obs)
for pos in X_POS:
    obs = Obstacles(pos, 160, "yellow")
    obstacles.append(obs)
for pos in X_POS:
    obs = Obstacles(pos, 125, "green")
    obstacles.append(obs)
for pos in X_POS:
    obs = Obstacles(pos, 90, "blue")
    obstacles.append(obs)
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")
while game_on:
    time.sleep(0.1)
    ball.move()
    screen.update()
    for obs in obstacles:
        if obs.ycor() - 14 <= ball.ycor() <= obs.ycor() + 14 and obs.xcor() - 42 <= ball.xcor() <= obs.xcor() + 42:
            ball.bounce_y()
            obs.goto(-500, 0)
    if ball.distance(paddle) < 35:
        ball.bounce_y()
    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.bounce_x()
    if ball.ycor() < - 290:
        life += 1
        ball.reset()
    if life == 3:
        result.game_over()
        game_on = False
    if ball.ycor() > 270:
        result.you_won()
        game_on = False
screen.exitonclick()
