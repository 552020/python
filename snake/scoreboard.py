from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.score = 0

    def show_score(self):
        # self.pendown()
        self.write('score: ' + str(self.score), move=False, align=ALIGNMENT, font=FONT)
        # self.penup()

    def add_point(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER' + str(self.score), move=False, align=ALIGNMENT, font=FONT)


