import time
from turtle import Screen, Turtle
from player_ship import PlayerShip
from aliens import Aliens
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=650)
screen.title("Space Invaders")
screen.tracer(0)

title_name = Turtle()
title_name.color("green")
title_name.hideturtle()
title_name.penup()
title_name.goto(-370, 280)
title_name.write(f'SPACE INVADERS', align="left", font=("Courier", 20, "bold"))

player_ship = PlayerShip()
scoreboard = Scoreboard()
aliens = Aliens()
screen.listen()
screen.onkey(player_ship.move_right, "Right")
screen.onkey(player_ship.create_laser_and_shoot, 'space')
screen.onkey(player_ship.move_left, "Left")

should_move_forward = True
game_is_on = True
time_speed_number = 0
while game_is_on:
    aliens.mega_alien()
    for alien in aliens.mega_aliens:
        if alien.xcor() >= 360:
            aliens.mega_aliens.remove(alien)
            alien.goto(10000, 10000)

    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_is_on = False

    player_ship.move_forward()
    aliens.alien_shoot_laser()
    aliens.laser1_move_forward()
    aliens.laser2_move_forward()
    aliens.laser3_move_forward()
    if player_ship.xcor() <= -350:
        player_ship.goto(-350, -260)

    elif player_ship.xcor() >= 350:
        player_ship.goto(350, -260)

    if len(aliens.aliens3) == 0:
        if len(aliens.aliens2) == 0:
            if len(aliens.aliens) == 0:
                scoreboard.game_won()
                game_is_on = False
            else:
                if aliens.aliens[-1].xcor() >= 350:
                    should_move_forward = True
                    aliens.alien_move_speed += 0.3

                if should_move_forward:
                    aliens.alien_move_forward()
                    aliens.alien2_move_forward()
                    aliens.alien3_move_forward()

                # Check a condition to stop the turtle from moving forward
                if aliens.aliens[0].xcor() <= -370:
                    should_move_forward = False
                    aliens.alien_move_speed += 0.3

                if not should_move_forward:
                    aliens.alien_move_backward()
                    aliens.alien2_move_backward()
                    aliens.alien3_move_backward()
        else:
            if len(aliens.aliens) == 0:
                if aliens.aliens2[-1].xcor() >= 350:
                    should_move_forward = True
                    aliens.alien_move_speed += 0.3

                if should_move_forward:
                    aliens.alien_move_forward()
                    aliens.alien2_move_forward()
                    aliens.alien3_move_forward()

                # Check a condition to stop the turtle from moving forward
                if aliens.aliens[0].xcor() <= -370:
                    should_move_forward = False
                    aliens.alien_move_speed += 0.3

                if not should_move_forward:
                    aliens.alien_move_backward()
                    aliens.alien2_move_backward()
                    aliens.alien3_move_backward()
            else:
                if aliens.aliens[-1].xcor() >= 350 or aliens.aliens2[-1].xcor() >= 350:
                    should_move_forward = True
                    aliens.alien_move_speed += 0.3

                if should_move_forward:
                    aliens.alien_move_forward()
                    aliens.alien2_move_forward()
                    aliens.alien3_move_forward()

                # Check a condition to stop the turtle from moving forward
                if aliens.aliens[0].xcor() <= -370 or aliens.aliens2[0].xcor() <= -370:
                    should_move_forward = False
                    aliens.alien_move_speed += 0.3

                if not should_move_forward:
                    aliens.alien_move_backward()
                    aliens.alien2_move_backward()
                    aliens.alien3_move_backward()
    else:
        if aliens.aliens[-1].xcor() >= 350 or aliens.aliens2[-1].xcor() >= 350 or aliens.aliens3[-1].xcor() >= 350:
            should_move_forward = True
            aliens.alien_move_speed += 0.3

        if should_move_forward:
            aliens.alien_move_forward()
            aliens.alien2_move_forward()
            aliens.alien3_move_forward()

        # Check a condition to stop the turtle from moving forward
        if aliens.aliens[0].xcor() <= -370 or aliens.aliens2[0].xcor() <= -370 or aliens.aliens3[0].xcor() <= -370:
            should_move_forward = False
            aliens.alien_move_speed += 0.3

        if not should_move_forward:
            aliens.alien_move_backward()
            aliens.alien2_move_backward()
            aliens.alien3_move_backward()

    screen.update()
    time.sleep(0.05)

    for laser in player_ship.lasers:
        for turtle in aliens.mega_aliens:
            if laser.distance(turtle) < 40:
                aliens.mega_aliens.remove(turtle)
                scoreboard.count_bonus_point()
                laser.goto(10000, 10000)
                turtle.goto(10000, 10000)

    for laser in player_ship.lasers:
        for lasers2 in aliens.lasers3:
            if laser.distance(lasers2) < 13:
                laser.goto(10000, 10000)
                lasers2.goto(10000, 10000)

    for laser in player_ship.lasers:
        for lasers in aliens.lasers2:
            if laser.distance(lasers) < 13:
                laser.goto(10000, 10000)
                lasers.goto(10000, 10000)

    for laser in player_ship.lasers:
        for lasers2 in aliens.lasers:
            if laser.distance(lasers2) < 13:
                laser.goto(10000, 10000)
                lasers2.goto(10000, 10000)

    for laser in player_ship.lasers:
        for alien in aliens.aliens3:
            if alien.distance(laser) < 30:
                aliens.aliens3.remove(alien)
                scoreboard.count_point()
                laser.goto(10000, 10000)
                alien.goto(10000, 10000)
        for alien in aliens.aliens2:
            if alien.distance(laser) < 30:
                aliens.aliens2.remove(alien)
                scoreboard.count_point()
                laser.goto(10000, 10000)
                alien.goto(10000, 10000)
        for alien in aliens.aliens:
            if alien.distance(laser) < 30:
                aliens.aliens.remove(alien)
                scoreboard.count_point()
                laser.goto(10000, 10000)
                alien.goto(10000, 10000)

        if laser.ycor() > 230:
            player_ship.lasers.remove(laser)
            laser.goto(10000, 10000)

    for laser in aliens.lasers:
        if laser.distance(player_ship) < 30:
            laser.goto(10000, 10000)
            scoreboard.count_lives()

    for laser in aliens.lasers2:
        if laser.distance(player_ship) < 30:
            laser.goto(10000, 10000)
            scoreboard.count_lives()

    for laser in aliens.lasers3:
        if laser.distance(player_ship) < 30:
            laser.goto(10000, 10000)
            scoreboard.count_lives()

screen.exitonclick()
