# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food=='grape' or food=='apple':
    print('fruit')
elif food=='bacon' or food=='steak':
    print('meat')
else:
    print('yuck')