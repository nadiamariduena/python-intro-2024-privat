#
# intro: imports
# import the random, string, and file containing the list of words
import random
import string
# when importing data from other files, keep in mind that the file type, is important
# because at the end of the first phase of this hangman exercise, i couldnt get the result i wanted  (no matter what word i used, it simply didnt get any word from the file of words), and was because the importing, i had this: "from file_withwords import words" and this file_withwords came from the file_withwords.py, so i ad the choice to either use the long name, or change the name to simply words, so to import it like "words" like here below(that is what i did)
from words import words



#  1
# create the function to grab the words from the list
def function_1_(words):

#   1.a grab the data coming from the 'words'
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
#  2)  create the function to init the hangman game
def function_2_hangman():

    #1 make the connection to the first function
    word =  function_1_(words)

    #2 TAKES the 'word' and turns it into a special list where each letter is only listed

    word_letters = set(word)
    #3 This line creates a list of all the letters in the alphabet, from A to Z. It’s like having a list of all the letters you can use to guess the secret word.
    alphabet = set(string.ascii_uppercase)
    # 4 This line starts with an empty list where you can keep track of the letters you’ve already guessed. At first, it’s empty because you haven’t guessed any letters yet.
    used_letters = set()

    #14 This line "sets up" a "variable" named "lives" to "keep track" of "how many attempts" the "player has left".
    lives = 0

    #
    #
    # 10 while the  length of word_letters list/array is greater `>` than zero, I am going to keep iterating
    while len(word_letters) > 0:
        #
        # 11 `.join` will turn the list into a **string**, separated by whatever the string is `you can add , white spaces, etc...`
        print("You have used these letters: ", ' '.join(used_letters))

        # -12 The code generates a new list, word_list,
        # - where each character in word is checked to see if it’s present in the collection used_letters.
        word_list = [letter if letter in used_letters else "_" for letter in word]
        # If the letter is in used_letters, it is included as-is in word_list, ELSE...
        # If the letter is not in used_letters, an underscore ("_") is included in its place.

        # 13 Now I am going to get this "new WORD list" and I am going to `.join()` it again(like i did it previously)
        print("Current word:", " ".join(word_list))
        # This part converts the word_list from a list of characters into a single string with each character separated by a space. For example, if word_list is ['h', 'e', 'l', 'l', '_'], " ".join(word_list) will produce "h e l l _"


        # 5 add var, (this var will be the letter the user will type) and assign message input to "guess a letter:" , to uppercase()
        user_letters = input("GUESS A LETTER: " ).upper()
        # 6) Check if the user letter is 'in' the alphabet, and hasnt - ' been used yet (used_letters)
        if user_letters in alphabet - used_letters:
            # 7) to the set of used letters '.add' the ( the user letter)
            used_letters.add(user_letters)

            ## 8 If the user_letters is 'in' the word letters...
            if user_letters in word_letters:
                # 9 to the set of word_letters, remove( the user_letters)
                word_letters.remove(user_letters)



        elif user_letters in used_letters:
            print("You have already used that character. Please try again")

        else:
            print("Invalid character. Please try again")

    # ____ 🟦  KEEP iterating until they find - all the letters





# ---- END ----
user_input = input("Type Something: ")
print(user_input)

if __name__ == '__main__':
    #
    # call the function with the condition logic
    function_2_hangman()
