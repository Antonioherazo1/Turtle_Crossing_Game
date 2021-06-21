import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
car = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        player.reset_position()
