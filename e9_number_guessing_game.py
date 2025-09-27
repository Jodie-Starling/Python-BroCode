import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print('Python Number Guessing Game')
print(f'Guess a number between {lowest_num} and {highest_num}')

while is_running:

    guess = input('Enter your guess: ')

    if guess.isdigit():
        guesses += 1
        guess = int(guess)
        if guess < lowest_num or guess > highest_num:
            print('Invalid guess')
            print(f'Please enter a number between {lowest_num} and {highest_num}')
        elif guess < answer:
            print('Too low')
        elif guess > answer:
            print('Too high')
        else:
            print('-----------------------------------')
            print(f'You guessed it! The answer was {answer}.')
            print(f'It took you {guesses} guesses')
            is_running = False
    else:
        print('Invalid guess')
        print(f'Please enter a number between {lowest_num} and {highest_num}')