from turtle import Turtle
FONT = ('Comic Sans MS', 25, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        # Initial score is set to be 0:
        self.score = 0
        # Opening the file to retrieve the highscore:
        file = open('data.txt')
        # The highscore is retrieved from the file:
        self.high_score = int(file.read())
        # File is then closed:
        file.close()
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 230)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}        High Score: {self.high_score}', font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Opening the file again to overwrite the highscore:
            with open('data.txt', mode='w') as file2:
                file2.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()



