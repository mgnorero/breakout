from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(arg=f"    Score : {self.score}    Lives : {self.lives}    High Score : {self.high_score}",
                   align="center", font=("Courier", 20, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def dead(self):
        self.lives -= 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.lives = 3
        self.update_scoreboard()



