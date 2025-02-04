from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.write(f'score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.write(f'score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def gameOver(self):
        self.goto(0, 0)
        self.write('Game Over!', align='center', font=('Arial', 24, 'normal'))