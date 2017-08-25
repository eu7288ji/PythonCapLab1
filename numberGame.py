import random

guessNumber = 0

number = random.randint(1, 10)
print('Guess a number between 1 and 10.')

while guessNumber == 0:

    guess = int(input('Your Guess: '))

    if guess < number:
        print('Too low...')

    if guess > number:
        print('Too high...')

    if guess == number:
        print('Cool. ')
        guessNumber = 1

