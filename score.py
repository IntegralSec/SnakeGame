from turtle import Turtle


class Score(Turtle):

    score = 0
    ALIGN = "Center"
    FONT = ('Courier', 18, 'normal')

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write_score(0)
        self.hideturtle()

    def increment(self):
        self.score += 1
        self.write_score(self.score)

    def get_score(self):
        return self.score

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} ", False, align=self.ALIGN, font=self.FONT)

    def write_score(self, value):
        self.clear()
        self.write(f"Score: {value} ", False, align=self.ALIGN, font=self.FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=self.ALIGN, font=self.FONT)

