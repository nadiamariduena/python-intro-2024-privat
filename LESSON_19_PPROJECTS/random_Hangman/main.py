import random
from file_withwords import words
import string


#1
def get_valid_word(words):
    #

    #
# 1 grab the data coming from the 'words'
    word = random.choice(words)
    # loop: add the condition in which you tell it to continue the loop if the users adds either a _ or ' ' (empty space)
    while '_' in word or ' ' in words:
        word = random.choice(words)
    # stop the loop
    return word


def hangman():
    #1 make the connection to the first function
    word = get_valid_word(words)

    #2 TAKES the 'word' and turns it into a special list where each letter is only listed
    word_letters = set(word)

    #
    #3 This line creates a list of all the letters in the alphabet, from A to Z. It’s like having a list of all the letters you can use to guess the secret word.
    alphabet = set(string.ascii_uppercase)

    #
    # 4 This line starts with an empty list where you can keep track of the letters you’ve already guessed. At first, it’s empty because you haven’t guessed any letters yet.
    used_letters = set()

    #
    #
    # 5 add var and assign message input to "guess a letter:" , to uppercase()
    user_letter = input("Guess a letter: ").upper()


    # CONDITION


    # 6 Check if the user letter is in the alphabet, and hasn't been used yet (used_letters)
    if user_letter in alphabet - used_letters:


        # 7 Add the user letter to the set of used letters
        used_letters.add(user_letter)

        ## 8 If the user letter is in the word letters...
        if user_letter in word_letters:

             # 9 If the user letter exist within the list of word_letters, remove it
            word_letters.remove(user_letter)


    elif user_letter in used_letters:
        print("You have already used that character. PLEASE try again.")


    else:
        print("Invalid character. Please try again")


user_input = input("Type Something")
print(user_input)

if __name__ == '__main__':
    hangman()

