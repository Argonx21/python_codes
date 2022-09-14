# game function returning high score value
def game():
    return 4


score = game()

with open("highScore.txt") as f:
     highScore = f.read()

if highScore == '':
    with open("highScore.txt","w") as f:
        f.write(str(score))

elif int(highScore)<score:
    with open("highScore.txt","w") as f:
        f.write(str(score))
