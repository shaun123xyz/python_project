from turtle import Turtle
ALIGNMENT = "center"



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=("Courier", 24, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.goto(0, 0)
        self.write(f"GAME OVER! Your final score:{self.score}", align=ALIGNMENT, font=("Courier", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
