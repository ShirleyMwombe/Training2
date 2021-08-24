import random

while True:
    choices = ['rock','paper','scissors']
    computer = random.choices(choices)
    player = None

    while player not in choices:
        player = input('rock,paper or scissors?: ').lower()
    if player == computer:
        print('Computer: ',computer)
        print('Player: ',player)
        print('TIE!!')
    elif player == 'rock':
        if computer == 'paper':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You lose!')
        if computer == 'scissors':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You Win!')
    elif player == 'paper':
        if computer == 'scissors':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You lose!')
        if computer == 'rock':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You Win!')
    elif player == 'scissors':
        if computer == 'rock':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You lose!')
        if computer == 'paper':
            print('Computer: ', computer)
            print('Player: ', player)
            print('You Win!')
    play_again = input('Play again? yes/no: ')
    if play_again != 'yes':
        break
print('Bye!')
