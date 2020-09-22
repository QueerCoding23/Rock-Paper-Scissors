#Rock Paper Scissors!

import time, random

turn = 0
pScore = 0
cScore = 0


def pause(number):
    time.sleep(number)


def text(string):
    print(string)
    pause(1)


def computerChoice():
    return random.randint(0, 2)


def playerChoice():
    choice = input("""  Rock, Paper, Scissors?
    >>> """)
    if choice.lower() == 'rock':
        return 0
    elif choice.lower() == 'paper':
        return 1
    elif choice.lower() == 'scissors':
        return 2
    else:
        return 'end'


def winCalc(player, computer):
    if player == 0:
        if computer == 0:
            return 'draw'
        elif computer == 1:
            return 'loss'
        else: 
            return 'win'
    elif player == 1:
        if computer == 0:
            return 'win'
        elif computer == 1:
            return 'draw'
        else: return 'loss'
    else:
        if computer == 0:
            return 'loss'
        elif computer == 1:
            return 'win'
        else: 
            return 'draw'


while True:
    text(f"""   Round: {turn}
    Your Score: {pScore}
    Computer Score: {cScore}""")

    pMove = playerChoice()
    if pMove == 'end':
        break
    cMove = computerChoice()
    playerState = winCalc(pMove, cMove)
    if playerState == 'win':
        pScore += 1
        text("Win!")
    elif playerState == 'loss':
        cScore += 1
        text("Loss...")
    else:
        text("Draw")
    turn += 1

if pScore > cScore:
    winner = "Player"
elif cScore > pScore:
    winner = "Computer"
else:
    winner = "Draw"
text(f"""   Total Rounds: {turn}
    Your final score: {pScore}
    Computer's final score: {cScore}
    Winner: {winner}""")