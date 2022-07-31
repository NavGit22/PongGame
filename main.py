from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True


# Display a Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game   ")
screen.tracer(0)

# Display a board separator
separator = Turtle()
separator.color('white')
separator.penup()
separator.goto(0, -300)
separator.setheading(90)

for i in range(60):
    if i % 2 == 0:
        separator.pendown()
    else:
        separator.penup()
    separator.forward(10)

separator.hideturtle()

# Display the Paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Display the ball
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

sleep_timer = 0.1
while game_is_on:
    screen.update()
    if sleep_timer < 0:
        sleep_timer = 0.1
    time.sleep(sleep_timer)
    ball.move()

    # Detect collision with wall
    if ball.check_wall():
        ball.bounce_y()

    # Detect collision with Right Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        sleep_timer -= 0.01
        ball.bounce_x()

    # Detect collision with Left Paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        sleep_timer -= 0.01
        ball.bounce_x()

    # Detect ball misses the Right Paddle
    if ball.check_ball_missed_right():
        ball.reset_ball()
        scoreboard.l_point()

    # Detect ball misses the left Paddle
    if ball.check_ball_missed_left():
        ball.reset_ball()
        scoreboard.r_point()



screen.exitonclick()