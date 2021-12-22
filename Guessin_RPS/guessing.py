from random import randint
answer=input('do you want to play the random guessing game? (yes/no) ')
if answer=='yes':
    Guess=int(input('Guess a number between 1 and 10 '))
    random= randint(1,10)
    while answer=='yes':
        if Guess < random:
            print('your guess is to low, try agian ')
            Guess=int(input('New Guess'))
        elif Guess>random:
            print('your guess is to high, try agian' )
            Guess=int(input('New Guess'))
        else:
            answer=input('congrate, you are correct, do you want to play agian?(yes/no)')
            if answer=='yes':
                random= randint(1,10)
                Guess=int(input('Guess a number between 1 and 10 '))
            else:
                print('okay, have a great day ')
                break
else:
    print('okay, have a great day ')
