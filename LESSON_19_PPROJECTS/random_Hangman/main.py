import random
from file_withwords import words
import string


#1
def get_valid_word(words):

    word = random.choice(words)
    while '_' in word or ' ' in words:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #
    #
    #
    user_letter = input("Guess a letter: ").upper()

    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)

        if user_letter in word_letters:
            word_letters.remove(user_letter)


    elif user_letter in used_letters:
        print("You have already used that character. PLEASE try again.")


    else:
        print("Invalid character. Please try again")


user_input = input("Type Something")
print(user_input)

if __name__ == '__main__':
    hangman()