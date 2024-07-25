

import random
from file_withwords import words
import string


#1
def get_valid_word():
    #2 retrieve the words from the file_withwords.py
    # 🔸 Initialization: this first random, will randomize the words in that file
    word = random.choice(words)


    # 🔸 Validation Loop
    # - The while loop checks the selected word (word) to ensure it does not contain underscores ('_') or spaces (' ').
    #
    # while _ or space '' is in the word, keep choosing a word (If the selected word contains either an underscore or a space, the loop continues to randomly select another word from words until a valid word (without underscores or spaces) is found.)
    while '_' in word or ' ' in words:

        # 🔶 Second Random Selection (random.choice(words) within the loop):
        word = random.choice(words)
        # 🔺 Inside the while loop, when word is found to contain an underscore or a space, random.choice(words) is used again to pick another random word from the list words.
        # - This process repeats until a word is selected that meets the condition of not containing underscores or spaces.

        return word
        # - Once a valid word (one that does not contain underscores or spaces) is found, the function returns this word.

def hangman():
  word = get_valid_word(words)  # This line gets a valid word to play with
  #
  #🟡 Creating Letters from the Word (set(word)):
  # Now that we have a word, let's look at the letters it's made of.
  #
  # - Imagine your word is "CAT".
  # - We take each letter from "CAT" (C, A, T) and write them down separately.
  # - This helps us keep track of which letters are in the word.
  word_letters = set(word)  # This line creates a set of letters from the chosen word




  #
  alphabet = set(string.ascii_uppercase)  # This line creates a set of all uppercase letters in the alphabet

#🟡 Making an Alphabet (set(string.ascii_uppercase)):
#
# In our game, we need to guess letters from A to Z
# - We call this the alphabet. It's like a list of all the letters we can use. So, we write down all these letters (A, B, C, ..., Z) on a piece of paper.