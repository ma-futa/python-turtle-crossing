from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    pass


class Car(Turtle):
    def __init__(self, color,y_coordinate):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(300, y_coordinate)

    def move(self):
        self.goto(self.xcor()-MOVE_INCREMENT, self.ycor())


