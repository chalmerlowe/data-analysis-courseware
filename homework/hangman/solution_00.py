WORD = 'darklord'
ALLOWED_GUESSES = 7

length = len(WORD)
answer = ['_'] * length
output_answer = ''.join(answer)
guesses = ['.'] * ALLOWED_GUESSES
output_guesses = ''.join(guesses)
guess_count = 0
total_guesses = length + ALLOWED_GUESSES

while total_guesses:
    print(output_answer, output_guesses)
    guess = input('Please guess a letter: ')
    
    if guess in WORD:
        count = WORD.count(guess)
        start = 0
        for cycle in range(count):
            index = WORD.find(guess, start)
            answer[index] = guess
            start = index + 1
    
    else:
        guesses[guess_count] = guess
        output_guesses = ''.join(guesses)
        guess_count += 1
        if guess_count == ALLOWED_GUESSES:
            print(output_answer, output_guesses)
            print('Game Over, try again!')
            break

    output_answer = ''.join(answer)
    if '_' not in output_answer:
        print('You win! Congratulations!')
        break
    
    total_guesses -= 1