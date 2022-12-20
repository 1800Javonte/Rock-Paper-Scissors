
import random

# Rock Paper Scissors Game
while True:
    choices =  ['rock','paper','scissors']

    cpu = random.choice(choices)
    player = None
    while player not in choices:
     player = input('Rock, Paper, or Scissors: ').lower()
    
    # User and computer pick the same choice
    if player == cpu:
        print('player: ' + player)
        print('cpu: ' + cpu)
        print('Tie')

        # Determine the winner when user picks rock
    elif player == 'rock':
        if cpu == 'paper':
            print('player: ' + player)
            print('cpu: ' + cpu)
            print('You lose!')
        if cpu == 'scissors':
            print('player: ' + player)
            print('cpu: ' + cpu)
            print('You win!')

            # Determine the winner if user picks scissors
    elif player == 'scissors':
        if cpu == 'paper':
            print('player: ' + player)
            print('cpu: ' + cpu)
            print('You win!')
        if cpu == 'rock':
            print('player: ' + player)
            print('cpu: ' + cpu)
            print('You lose!')

            # Determine the winner if user picks paper
    elif player == 'paper':
        if cpu == 'scissors':
            print('player: ' + player)
            print('cpu: ' + cpu)
            print('You lose!')
        if cpu == 'rock':
            print('player: ' + player)
            print('cpu: ' + cpu)
            print('You win!')
    
    # See if the user wants to play again
    play_again = input('Do you want to play again? (yes or no): ').lower()
    if play_again != 'yes':
        break
print('Thanks for playing!')