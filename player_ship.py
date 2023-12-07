from turtle import Turtle
# from scoreboard import Scoreboard


class PlayerShip(Turtle):
    def __init__(self):
        super().__init__()
        # scoreboard = Scoreboard()
        # self.remaining = scoreboard.lives
        # self.remaining_x = -370
        # self.remaining_y = -270
        # for num in range(self.remaining):
        #     remaining_turtles = Turtle()
        #     remaining_turtles.shape("square")
        #     remaining_turtles.color("blue")
        #     remaining_turtles.shapesize(stretch_wid=0.7, stretch_len=3)
        #     remaining_turtles.penup()
        #     remaining_turtles.goto(self.remaining_x, self.remaining_y)
        #     self.remaining_x += 50

        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=0.7, stretch_len=3)
        self.penup()
        self.goto(0, -260)
        self.lasers = []
        self.laser_move_speed = 8

    def move_right(self):
        x = self.xcor() + 20
        self.goto(x, self.ycor())

    def move_left(self):
        x = self.xcor() - 20
        self.goto(x, self.ycor())

    def create_laser_and_shoot(self):
        if len(self.lasers) >= 1:
            pass
        else:
            if len(self.lasers) < 1:
                laser = Turtle()
                laser.color("red")
                laser.shape('square')
                laser.shapesize(stretch_wid=0.8, stretch_len=0.2)
                laser.penup()
                laser.goto(self.xcor(), self.ycor() + 13)
                self.lasers.append(laser)

    def move_forward(self):
        for laser in self.lasers:
            y = laser.ycor() + self.laser_move_speed  # Adjust the value to control the speed of the laser
            laser.sety(y)
