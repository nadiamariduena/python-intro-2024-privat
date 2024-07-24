
import random
from words import words


# This function chooses a valid word from a list of words.
def get_valid_word(words):
    # Choose a random word from the list of words.
    word = random.choice(words)

    # Check if the chosen word contains '~' or ' '.
    # If it does, choose another random word until a valid one is found.
    while '~' in word or ' ' in word:
        word = random.choice(words)

    # Return the valid word without any '~' or ' ' characters.
    return word
