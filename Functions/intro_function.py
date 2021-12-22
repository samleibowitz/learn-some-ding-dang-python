colors=['red','orange','yellow','blue']


# function struction def name_of_function ():
                            #indent code



def say_hi():
    print('Hi')


def square_of_7():
    return 7**2  # once return is hit, the function ends






from random import random


def flip_coin():
    #generate random number 0-1
    t=random()
    if t>.5:
        print('heads')
    else:
        print('tails')