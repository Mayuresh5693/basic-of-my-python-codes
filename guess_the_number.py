import random

def guess(n):
    random_number = random.randint(1,n)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {n}:  ' ))
        if guess < random_number :
            print ('Sorry the number is too low ,Try again')
        elif guess > random_number:
            print ('Sorry the number is too high ,Try again')
    print (f'congrats,you guess {random_number} correctly')

guess(100)
