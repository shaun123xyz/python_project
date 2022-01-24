from turtle import Turtle


class Bat(Turtle):
     
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(x_position, y_position)
        
    # move up
    def up(self):
        new_y = self.ycor() + 20
        self.setpos(self.xcor(), new_y)

    #move down
    def down(self):
        new_y = self.ycor() - 20
        self.setpos(self.xcor(), new_y)