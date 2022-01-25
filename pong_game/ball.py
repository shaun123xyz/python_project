from turtle import Turtle
import random

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
        
    # bounce the ball off the wall
    def wall_bounce(self):
        self.y_move *= -1
        
    #bounce off the bat
    def bat_bounce(self):
        self.x_move *= -1
        if self.x_move > 0:
            self.x_move += 0.05
        else:
            self.x_move -= 0.05
        if self.y_move > 0:
            self.y_move += 0.05
        else:
            self.y_move -= 0.05
        
    #reset the ball position    
    def reset_p(self):
        self.goto(0, 0)
        self.x_move = random.choice((0.1, -0.1))
        self.y_move = random.choice((0.1, -0.1))
        
        