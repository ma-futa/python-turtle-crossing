import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

# car_manager code
list_of_cars = []
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# end of car_manager code

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.game_speed)
    screen.update()
    # car_manager code
    if random.randint(1,10) == 3:
        for index in range(random.randint(2,4)):
            car = Car(random.choice(COLORS), random.randrange(-250, 250, 20))
            list_of_cars.append(car)

    for car in list_of_cars:
        car.move()
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    # end of car_manager code
    # when turtle reaches screens end
    if player.ycor() >= screen.window_height()//2:
        player.reset()
        scoreboard.increase_score()

screen.exitonclick()
