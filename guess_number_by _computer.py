import random

def guess_by_computer(n):

    low = 1
    high = n
    feedback = ''
  
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f'is {guess} is too high type (h) / is too low type (l) / is correct type (c) : ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'congrats!! computer guessed your number , {guess} , correctly')


guess_by_computer(10)

