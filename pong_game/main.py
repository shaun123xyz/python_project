from turtle import Screen, Turtle
from bat import Bat

# Setup the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Bong Game")
screen.tracer(0)

# Have two bat on screen
left_bat = Bat(-350,0)
right_bat = Bat(350,0)





# Repond to key pressed
screen.listen()
screen.onkey(left_bat.up, "w")
screen.onkey(left_bat.down, "s")
screen.onkey(right_bat.up, "Up")
screen.onkey(right_bat.down, "Down")


# Run the game
game_on = True
while game_on:
    screen.update()




screen.exitonclick()




