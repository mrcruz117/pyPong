from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move()

    # top/bottom wall collision
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        # bounce
        ball.bounce_y()
        print("bounce")

    # detect collision with r_paddle
    if (ball.distance(r_paddle) <= 50 and ball.xcor() >= 340) or (
            ball.distance(l_paddle) <= 50 and ball.xcor() <= -340):
        ball.bounce_x()
        print("contact")

    # if ball.distance(l_paddle) <= 50 and ball.xcor() <= -340:
    #     ball.bounce_x()
    #     print("contact")

screen.exitonclick()
