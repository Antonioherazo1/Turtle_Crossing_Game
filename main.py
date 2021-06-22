import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
loop_create_car = 0

while game_is_on:
    time.sleep(player.vel)
    screen.update()
    loop_create_car += 1

    car_manager.move_cars()

    if player.ycor() > 280:
        player.reset_position()

    while loop_create_car > 6:
        car_manager.create_car()
        loop_create_car = 0

    for car in car_manager.cars:
        if player.distance(car) < 28:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 250:
        player.reset_position()
        scoreboard.inc_level()


screen.exitonclick()
