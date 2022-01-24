from turtle import Turtle


class Ball(Turtle):
     
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()