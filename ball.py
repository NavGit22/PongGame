from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def check_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return True

    def check_ball_missed_right(self):
        if self.xcor() > 380:
            return True

    def check_ball_missed_left(self):
        if self.xcor() < -380:
            return True

    def reset_ball(self):
        if self.xcor() > 300:
            self.x_move = -10
            self.y_move = -10
            self.goto(0, 0)

        if self.xcor() < -300:
            self.x_move = 10
            self.y_move = 10
            self.goto(0, 0)

