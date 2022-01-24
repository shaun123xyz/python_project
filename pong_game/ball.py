from turtle import Turtle


class Ball(Turtle):
     
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 0.1
        self.y_move = 0.1
        
    # move the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    # bounce the ball
    def wall_bounce(self):
        self.y_move *= -1
        
    def bat_bounce(self):
        self.x_move *= -1