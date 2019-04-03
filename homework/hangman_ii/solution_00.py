import random


with open('words.txt') as fin:
    lines = fin.readlines()
    words = []
    for line in lines:
        words.append(line.strip())

WORD = random.choice(words)

ALLOWED_GUESSES = 7

def display(chars):
    return ''.join(chars)

def char_generator(length, char='_',):
    return [char] * length

def replay():
    response = input('Would you like to replay? (y/n): ')
    if response == 'y':
        return True
    return False


answer = char_generator(len(WORD))
guesses = char_generator(ALLOWED_GUESSES, char='.')
guess_count = 0

while True:
    print(display(answer), display(guesses))
    guess = input('Please guess a letter: ')
    included = False

    for index, letter in enumerate(WORD):
        if letter == guess:
            answer[index] = guess
            included = True
            
    if '_' not in answer:
        print('{}\nYou win! Congratulations!'.format(display(answer)))
        if not replay():
            break
        WORD = random.choice(words)
        answer = char_generator(len(WORD))
        guesses = char_generator(ALLOWED_GUESSES, char='.')
        guess_count = 0
    
    if included == False:
        guesses[guess_count] = guess
        guess_count += 1
        if guess_count == ALLOWED_GUESSES:
            print('{} {}\nGame Over, try again!'.format(display(answer),
                                                        display(guesses)))
            if not replay():
                break
             
            WORD = random.choice(words)
            answer = char_generator(len(WORD))
            guesses = char_generator(ALLOWED_GUESSES, char='.')
            guess_count = 0
