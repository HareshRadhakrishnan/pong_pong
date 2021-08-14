from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time
screen = Screen()
score_board = ScoreBoard()
screen.bgcolor("black")
screen.setup(width=800, height=600)
ball = Ball()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0) )
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_on = True
while game_on:
    time.sleep(ball.speed_num)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() < -390:
        score_board.r_point()
        ball.reposition()
    elif ball.xcor() > 390:
        score_board.l_point()
        ball.reposition()

screen.exitonclick()