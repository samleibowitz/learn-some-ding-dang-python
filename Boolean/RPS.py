from random import randbytes, randint, random
player1_input=input('Please enter rock,paper or scissor ')
possible_input= ['rock','paper','scissor']
player2_input=possible_input[randint(0,2)]
print(f'player 2 chose {player2_input}')



if player1_input == 'rock':
        if player2_input == 'rock':
            print(' you both chose rock, its a tie')
        elif player2_input == 'paper':
            print('player 2 won with paper and you lost with rock')
        else:
            print('you won with rock and player 2 lost with scissor')
elif player1_input == 'paper':
        if player2_input == 'paper':
            print(' you both chose paper, its a tie')
        elif player2_input == 'scissor':
            print('player 2 won with scissor and you lost with paper')
        else:
            print('you won with paper and player 2 lost with Rock')

else:
        if player2_input == 'scissor':
            print(' you both chose scissor, its a tie')
        elif player2_input == 'rock':
            print('player 2 won with rock and you lost with scissor')
        else:
            print('you won with scissor and player 2 lost with paper')


