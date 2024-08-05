```python

#🟡  fill each comment, analyse the comments, dont copy, just think, if you started with javascript the syntax in python will confuse you,  but at the end is the same logic

#🔴 repeat this 20 times until you get familiar with the syntax

# -----------------------------------
# intro: imports
# import the random, string, and file containing the list of words
import random
import string
from file_withwords import words



# 🟦 0
# create the function to grab the words from the list
def function_1_(words):

# 🟦 1.a grab the data coming from the 'words'
## Pick a random word from the list

    word = random.choice(words)

    # 1.b loop: add the condition in which you tell it:
    ## If the word has underscores or spaces...

    while "_" in word or " " in words:

        # 1.c # ... Pick a new word
        word = random.choice(words)


    # 1.d # Give back the chosen word

    return word


#------------
# 🟧 # create the function to init the hangman game
def function_2_hangman():

    #1 make the connection to the first function
    word =  function_1_(words)

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
    # 5 add var, (this var will be the letter the user will type) and assign message input to "guess a letter:" , to uppercase()


    user_letters = input("GUESS A LETTER" ).upper()


    # CONDITION


     # 6 Check if the user letter is 'in' the alphabet, and hasnt - ' been used yet (used_letters)


    if user_letters in alphabet - used_letters:

        # 7 to the set of used letters '.add' the ( the user letter)
        used_letters.add(user_letters)

        ## 8 If the user_letters is 'in' the word letters...
        if user_letters in word_letters:


                  # 9 to the set of word_letters, remove( the user_letters)
             word_letters.remove(user_letters)

    elif user_letters in used_letters:
        print("You have already used that character. Please try again")

    else:
        print("Invalid character. Please try again")

user_input = input("Type Something")
print(user_input)

if __name__ == '__main__':
    function_2_hangman()

```