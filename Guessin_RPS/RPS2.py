from random import randbytes, randint, random
player1_input=input('Please enter rock,paper or scissor ')
possible_input= ['rock','paper','scissor']
player2_input=possible_input[randint(0,2)]
print(f'player 2 chose {player2_input}')
answer=None

while answer!='no':
    if player1_input == 'rock':
            if player2_input == 'rock':
                 print(' you both chose rock, its a tie')
                 answer=input('do you want to play agiain (yes/no) ')
                 if answer=='yes':
                    player1_input=input('Please enter rock,paper or scissor ')
                    player2_input=possible_input[randint(0,2)]
                 else:
                    print('Okay have a great day')
                    break
            elif player2_input == 'paper':
                print('player 2 won with paper and you lost with rock')
                answer=input('do you want to play agiain (yes/no')
                if answer=='yes':
                    player1_input=input('Please enter rock,paper or scissor ')
                    player2_input=possible_input[randint(0,2)]
                else:
                    print('Okay have a great day')
                    break
            else:
                print('you won with rock and player 2 lost with scissor')
                answer=input('do you want to play agiain (yes/no')
                if answer=='yes':
                    player1_input=input('Please enter rock,paper or scissor ')
                    player2_input=possible_input[randint(0,2)]
                else:
                    print('Okay have a great day')
                    break

    elif player1_input == 'paper':
            if player2_input == 'paper':
                print(' you both chose paper, its a tie')
                answer=input('do you want to play agiain (yes/no')
                if answer=='yes':
                    player1_input=input('Please enter rock,paper or scissor ')
                    player2_input=possible_input[randint(0,2)]
                else:
                    print('Okay have a great day')
                    break

            elif player2_input == 'scissor':
                print('player 2 won with scissor and you lost with paper')
                answer=input('do you want to play agiain (yes/no')
                if answer=='yes':
                    player1_input=input('Please enter rock,paper or scissor ')
                    player2_input=possible_input[randint(0,2)]
                else:
                    print('Okay have a great day')
                    break

            else:
                print('you won with paper and player 2 lost with Rock')
                answer=input('do you want to play agiain (yes/no')
                if answer=='yes':
                    player1_input=input('Please enter rock,paper or scissor ')
                    player2_input=possible_input[randint(0,2)]
                else:
                    print('Okay have a great day')
                    break


    else:
            if player2_input == 'scissor':
                 print(' you both chose scissor, its a tie')
                 answer=input('do you want to play agiain (yes/no')
                 if answer=='yes':
                    player1_input=input('Please enter rock,paper or scissor ')
                    player2_input=possible_input[randint(0,2)]
                 else:
                    print('Okay have a great day')
                    break

            elif player2_input == 'rock':
                print('player 2 won with rock and you lost with scissor')
                answer=input('do you want to play agiain (yes/no')
                if answer=='yes':
                    player1_input=input('Please enter rock,paper or scissor ')
                    player2_input=possible_input[randint(0,2)]
                else:
                    print('Okay have a great day')
                    break

            else:
             print('you won with scissor and player 2 lost with paper')
             answer=input('do you want to play agiain (yes/no')
             if answer=='yes':
                    player1_input=input('Please enter rock,paper or scissor ')
                    player2_input=possible_input[randint(0,2)]
             else:
                    print('Okay have a great day')
                    break

