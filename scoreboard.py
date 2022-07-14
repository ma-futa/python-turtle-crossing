from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, ):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.level = 0
        self.display_score()
        self.game_speed = 0.1

    def display_score(self):
        self.clear()
        self.write(f'LEVEL: {self.level}', align='center', font=FONT)

    def increase_score(self):
        self.level += 1
        self.display_score()
        self.increase_game_speed()

    def increase_game_speed(self):
        self.game_speed *= 0.5
        print(self.game_speed)

    # come back and finish gameover
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=FONT)
