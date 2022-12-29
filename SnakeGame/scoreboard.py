from turtle import Turtle
ALIGN="center"
FONT=("arial",24,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.scoreupdate()

    def score_increase(self):
        self.score += 1
        self.clear()
        self.scoreupdate()
    def scoreupdate(self):
        self.write(f"score:{self.score}", align=ALIGN, font=FONT)

    def gameover(self):
        self.clear()
        self.write("GAME OVER",align =ALIGN,font=FONT)