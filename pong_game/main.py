from turtle import Screen, Turtle
from bat import Bat
from ball import Ball
from score import Score

# Setup the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Bong Game")
screen.tracer(0)

# Have two bat on screen
left_bat = Bat(-350,0)
right_bat = Bat(350,0)
ball = Ball()
score = Score()




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
    ball.move()

    # Collision with the walls
    if abs(ball.ycor()) > 280:
        ball.wall_bounce()
        
    # collosion with Bat
    if (ball.distance(right_bat) < 50 and ball.xcor() > 320) or (ball.distance(left_bat) < 50 and ball.xcor() < -320):
           ball.bat_bounce()
           

    #Detect right player misses the ball
    if ball.xcor() > 380:
        ball.reset_p()
        score.left_point()


    #Detect left player misses the ball
    if ball.xcor() < -380:
        ball.reset_p()
        score.right_point()
       



screen.exitonclick()




