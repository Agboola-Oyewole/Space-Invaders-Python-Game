import random
from turtle import Turtle


class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.lasers = []
        self.lasers2 = []
        self.lasers3 = []
        self.mega_aliens = []
        self.laser_move_speed = 6
        self.aliens = []
        self.aliens2 = []
        self.aliens3 = []
        self.y1 = 150
        self.x1 = 0
        self.y2 = 100
        self.x2 = 0
        self.y3 = 50
        self.x3 = 0
        self.alien_move_speed = 6
        for num in range(0, 7):
            alien = Turtle()
            alien.color("green")
            alien.shape('turtle')
            alien.penup()
            alien.goto(self.x1, self.y1)
            self.x1 += 50
            self.aliens.append(alien)

        for num in range(0, 7):
            alien = Turtle()
            alien.color("green")
            alien.shape('turtle')
            alien.penup()
            alien.goto(self.x2, self.y2)
            self.x2 += 50
            self.aliens2.append(alien)

        for num in range(0, 7):
            alien = Turtle()
            alien.color("green")
            alien.shape('turtle')
            alien.penup()
            alien.goto(self.x3, self.y3)
            self.x3 += 50
            self.aliens3.append(alien)

    def mega_alien(self):
        random_chance2 = random.randint(1, 300)
        if random_chance2 == 4:
            if len(self.mega_aliens) > 0:
                pass
            else:
                alien = Turtle()
                alien.color("green")
                alien.shape('turtle')
                alien.penup()
                alien.turtlesize(2, 2)
                alien.goto(-370, 220)
                self.mega_aliens.append(alien)

        for alien in self.mega_aliens:
            alien.forward(3)

    def alien_move_forward(self):
        for alien in self.aliens:
            alien.backward(self.alien_move_speed)

    def alien_move_backward(self):
        for alien in self.aliens:
            alien.forward(self.alien_move_speed)

    def alien2_move_forward(self):
        for alien in self.aliens2:
            alien.backward(self.alien_move_speed)

    def alien2_move_backward(self):
        for alien in self.aliens2:
            alien.forward(self.alien_move_speed)

    def alien3_move_forward(self):
        for alien in self.aliens3:
            alien.backward(self.alien_move_speed)

    def alien3_move_backward(self):
        for alien in self.aliens3:
            alien.forward(self.alien_move_speed)

    def alien_shoot_laser(self):
        random_chance1 = random.randint(1, 45)
        if len(self.aliens) <= 1:
            pass
        else:
            random_alien = random.randint(0, len(self.aliens) - 1)
            if random_chance1 == 1:
                laser = Turtle()
                laser.color("green")
                laser.shape('square')
                laser.shapesize(stretch_wid=0.8, stretch_len=0.2)
                laser.penup()
                laser.goto(self.aliens[random_alien].xcor(), self.aliens[random_alien].ycor() - 13)
                self.lasers.append(laser)

        random_chance2 = random.randint(1, 45)
        if len(self.aliens2) <= 1:
            pass
        else:
            random_alien = random.randint(0, len(self.aliens2) - 1)
            if random_chance2 == 1:
                laser = Turtle()
                laser.color("green")
                laser.shape('square')
                laser.shapesize(stretch_wid=0.8, stretch_len=0.2)
                laser.penup()
                laser.goto(self.aliens2[random_alien].xcor(), self.aliens2[random_alien].ycor() - 13)
                self.lasers2.append(laser)

        random_chance3 = random.randint(1, 45)
        if len(self.aliens3) <= 1:
            pass
        else:
            random_alien = random.randint(0, len(self.aliens3) - 1)
            if random_chance3 == 1:
                laser = Turtle()
                laser.color("green")
                laser.shape('square')
                laser.shapesize(stretch_wid=0.8, stretch_len=0.2)
                laser.penup()
                laser.goto(self.aliens3[random_alien].xcor(), self.aliens3[random_alien].ycor() - 13)
                self.lasers3.append(laser)

    def laser1_move_forward(self):
        for laser in self.lasers:
            y = laser.ycor() - self.laser_move_speed  # Adjust the value to control the speed of the laser
            laser.sety(y)

    def laser2_move_forward(self):
        for laser in self.lasers2:
            y = laser.ycor() - self.laser_move_speed  # Adjust the value to control the speed of the laser
            laser.sety(y)

    def laser3_move_forward(self):
        for laser in self.lasers3:
            y = laser.ycor() - self.laser_move_speed  # Adjust the value to control the speed of the laser
            laser.sety(y)
