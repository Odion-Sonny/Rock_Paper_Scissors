# Rock, Paper, Scissors
import random
def rps():
    
    keep_playing = True

    while keep_playing is True:
        player_input = input('Enter r, p, s for Rock, Paper or Scissors respectively: ')
        possible_actions = ['r', 'p', 's']
        computer_input = random.choice(possible_actions)
        in_full = {'r':'Rock', 'p':'Paper', 's':'Scissors'}
        print(f'You chose {in_full[user_input]} and the computer chose {in_full[computer_input]}')

        ''' 
        Edge cases
          - same input
          - different inputs
        '''
        
        if player_input == computer_input:
            print(f"Both players chose {player_input}, it's a tie")
        elif player_input == 'r':
            if computer_input == 's':
                print('Rock smashes Scissors, you win')
            else:
                print('Paper covers Rock, computer wins')
        elif player_input == 'p':
            if computer_input == 'r':
                print('Paper covers Rock, you win')
            else:
                print('Scissors cuts Paper, computer wins')
        elif player_input == 's':
            if computer_input == 'p':
                print('Scissors cuts Paper, you win')
            else:
                print('Rock smashes Scissors, computer wins')
        
        choice = input('Would you like to keep playing?:[y/n] ')
        if choice == 'y':
            keep_playing= True
        elif choice == 'n':
            keep_playing = False
rps()
