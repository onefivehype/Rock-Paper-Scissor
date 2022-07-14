import random
iscore = 0
oscore = 0
while True:
    choices = ['ROCK', 'PAPER', 'SCISSOR']
    RPS = random.choice(choices)
    iRPS = input('ROCK, PAPER or SCISSOR: ')

    if iRPS == RPS:
        print('Opponent gave', RPS)
        print('TIE!!')
        print('YOUR SCORE-', iscore)
        print('OPPONENT SCORE-', oscore)
        continue

    elif iRPS == 'ROCK' and RPS == 'PAPER':
        print('Opponent gave', RPS)
        print('YOU LOOSE')
        oscore = oscore + 1
        print('YOUR SCORE-', iscore)
        print('OPPONENT SCORE-', oscore)
        continue
    elif iRPS == 'ROCK' and RPS == 'SCISSOR':
        print('Opponent gave', RPS)
        print('YOU WIN')
        iscore = iscore + 1
        print('YOUR SCORE-', iscore)
        print('OPPONENT SCORE-', oscore)
        continue

    elif iRPS == 'PAPER' and RPS == 'ROCK':
        print('Opponent gave', RPS)
        print('YOU WIN')
        iscore = iscore + 1
        print('YOUR SCORE-', iscore)
        print('OPPONENT SCORE-', oscore)
        continue
    elif iRPS == 'PAPER' and RPS == 'SCISSOR':
        print('Opponent gave', RPS)
        print('YOU LOOSE')
        oscore = oscore + 1
        print('YOUR SCORE-', iscore)
        print('OPPONENT SCORE-', oscore)
        continue

    elif iRPS == 'SCISSOR' and RPS == 'ROCK':
        print('Opponent gave', RPS)
        print('YOU LOOSE')
        oscore = oscore + 1
        print('YOUR SCORE-', iscore)
        print('OPPONENT SCORE-', oscore)
        continue
    elif iRPS == 'SCISSOR' and RPS == 'PAPER':
        print('Opponent gave', RPS)
        print('YOU WIN')
        iscore = iscore + 1
        print('YOUR SCORE-', iscore)
        print('OPPONENT SCORE-', oscore)
        continue
    else:
        break
print('DONE')
