import random

questions = ['What is the capital of France?',
             'What is 2 + 2?',
             'What country is Miranda Kerr from?',
             'Which city is the Capital of the World?',
             'What year was the Statue of Liberty officially dedicated and opened to the public?']


options = [['A. London', 'B. Paris', 'C. New York'],
            ['A. 3', 'B. 4', 'C. 5'],
            ['A. USA', 'B. Australia', 'C. Canada'],
            ['A. Los Angeles', 'B. London', 'C. New York'],
            ['A. 1876', 'B. 1886', 'C. 1901']]

answers = ['B', 'B', 'B', 'C', 'B']
guesses = []
score = 0
question_num = 0

for question in questions:
    print('-------------------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('Enter (A, B, or C): ').upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print('CORRECT!')
    else:
        print('WRONG!')
        print(f'The correct answer is: {answers[question_num]}')
    question_num += 1

print('-------------------------')
print('         RESULTS         ')
print('-------------------------')

print('Answers: ', end='')
for answer in answers:
    print(answer,end = ' ')
print()
print('Guesses: ', end='')
for guess in guesses:
    print(guess, end=' ')
print()
score = int((score / len(questions)) * 100)
print(f'Your score is: {score}%')