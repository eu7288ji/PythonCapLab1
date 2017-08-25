import random #random generator

guessNumber = 0 #variable for user guess

number = random.randint(1, 10) #thinks of random int between 1 and 10
print('Guess a number between 1 and 10.')

while guessNumber == 0:
#looping through every time the user guesses between 1 and 10
    guess = int(input('Your Guess: '))

    if guess < number: #if under, too low
        print('Too low...')

    if guess > number: #if over, too high
        print('Too high...')

    if guess == number: #when guessed right, they are congratulated
        print('Cool. ')
        guessNumber = 1

