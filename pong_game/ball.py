from turtle import Turtle


class Ball(Turtle):
     
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        
    # move the ball
    def move(self):
        new_x = self.xcor() + 0.1
        new_y = self.ycor() + 0.1
        self.goto(new_x, new_y)