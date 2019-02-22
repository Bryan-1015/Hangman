
import random
from hangman_list import text_w


def gallows(penal):
    if penal == 0:
        gal = "-------I \n" \
              "       I \n" \
              "       I \n" \
              "       I \n" \
              "       I \n" \
              "       I \n" \
              "       I \n" \
              "      / \ \n " \
              "     /   \ \n " \
              "     ===== \n"
    if penal == 1:
        gal = "-------I \n" \
              " I     I \n" \
              "       I \n" \
              "       I \n" \
              "       I \n" \
              "       I \n" \
              "       I \n" \
              "      / \ \n " \
              "     /   \ \n " \
              "     ===== \n"
    if penal == 2:
        gal = "-------I \n" \
              " I     I \n" \
              " O     I \n" \
              "       I \n" \
              "       I \n" \
              "       I \n" \
              "       I \n" \
              "      / \ \n " \
              "     /   \ \n " \
              "     ===== \n"
    if penal == 3:
        gal = "-------I \n" \
              "  I    I \n" \
              "  O    I \n" \
              " /|\   I \n" \
              "       I \n" \
              "       I \n" \
              "       I \n" \
              "      / \ \n " \
              "     /   \ \n " \
              "     ===== \n"
    if penal == 4:
        gal = "-------I \n" \
              "  I    I \n" \
              "  O    I \n" \
              " /|\   I \n" \
              "  |    I \n" \
              "       I \n" \
              "       I \n" \
              "      / \ \n " \
              "     /   \ \n " \
              "     ===== \n"
    if penal == 5:
        gal = " -------I \n" \
              "  I     I \n" \
              "  O     I \n" \
              " /|\    I \n" \
              "  |     I \n" \
              "  |     I \n" \
              "        I \n" \
              "       / \ \n " \
              "      /   \ \n " \
              "      ===== \n"
    if penal == 6:
        gal = " -------I \n" \
              "  I     I \n" \
              "  O     I \n" \
              " /|\    I \n" \
              "  |     I \n" \
              "  |     I \n" \
              "   \    I \n" \
              "       / \ \n " \
              "      /   \ \n " \
              "      ===== \n"
    if penal == 7:
        gal = " -------I \n" \
              "  I     I \n" \
              "  O     I \n" \
              " /|\    I \n" \
              "  |     I \n" \
              "  |     I \n" \
              " / \    I \n" \
              "       / \ \n " \
              "      /   \ \n " \
              "      ===== \n"
        return gal

again ='y'
while again == 'y':

# Choose a random word from the text_w
    index = random.randint(0,len(text_w))
    word = text_w[index]
    secret_word = list(word)
    #print(secret_word)
    new_word = ['*' for i in range (len(secret_word))] # The letters of hangman is converted to '*'
    print(new_word)
    penalty = 0 # When you begin the game you start with 0 penalty
    letter_used = []
    while '*' in new_word and penalty < 7: # If you get the wrong letter 7 times the game will end
        guess = input('Enter a letter \n')
        if guess not in secret_word or guess in letter_used:
            penalty += 1 # If you don't a letter or if choosing the same letter twice that you get a penalty

        else: # This block shows that if you guess the letter correct it changes '*' to the letter in the secret_word
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    new_word[i] = secret_word[i]
        letter_used.append(guess)
        print(letter_used)
        print(new_word)
        print('penalty', penalty) # Here we will be placed the gallows call
    print(gallows(penalty))
    again = input('If you want to keep playing , press y,else,press n \n')
    print('Thank you for playing hangman! See you next time!')