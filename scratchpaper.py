

word = 'hangman'
secret_word = list(word)
print(secret_word)
new_word = ['*' for i in range (len(secret_word))]
print(new_word)
penalty = 0
letter_used = []
while '*' in new_word and penalty < 7:
    guess = input('Enter a letter \n')
    if guess not in secret_word or guess in letter_used:
        penalty += 1

    else:
        for i in range(len(secret_word)):
            if guess == secret_word[i]:
                new_word[i] = secret_word[i]
    letter_used.append(guess)
    print(letter_used)
    print('penalty', penalty)
    print(new_word)