import random

def guser_uess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f'Guess a number between  1 and {x}: '))
        if guess < random_number:
            print(f'Sorry, guess again. That is too low!')
        elif guess > random_number:
            print('Sorry,guess again. That is too high')
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!')


def computer_guess(y):
    low = 1
    high = y
    feedback = ''

    while  feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback=input(f'Is {guess} too high (H), too low (L), or Correct (C)?').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f'Yay! The computer gussed your number, {guess}, correctly!')
computer_guess(20)
#user_guess(10)