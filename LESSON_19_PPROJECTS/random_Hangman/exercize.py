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


    #
    # 4 This line starts with an empty list where you can keep track of the letters you’ve already guessed. At first, it’s empty because you haven’t guessed any letters yet.


    #
    #
    # 5 add var and assign message input to "guess a letter:" , to uppercase()



    # CONDITION


    # 6 Check if the user letter is in the alphabet, and hasn't been used yet (used_letters)



        # 7 Add the user letter to the set of used letters


        ## 8 If the user letter is in the word letters...


             # 9 If the user letter exist within the list of word_letters, remove it

