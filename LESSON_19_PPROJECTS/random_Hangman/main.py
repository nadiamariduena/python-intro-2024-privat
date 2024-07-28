#
# intro: imports
# import the random, string, and file containing the list of words
import random


from words import words
from hangman_visual import lives_visual_dict
import string


#  1
#
def function_1_(words):
    word = random.choice(words)
    while "_" in word or " " in words:
        word = random.choice(words)
    return word.upper()


#  2)
def function_2_hangman():

    word =  function_1_(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()


    lives = 7

    #________**
    while len(word_letters) > 0 and lives > 0:


        print('You have', lives,  'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word:", ' '.join(word_list))

        user_letters = input("GUESS A LETTER: " ).upper()
        #________**
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                lives = lives - 1
                print("Letter is not in word")
                print('\nYour letter,', user_letters, 'is not in the word.')
        #________
        elif user_letters in used_letters:
            print("You have already used that character. Please try again")
        else:
            print("Invalid character. Please try again")


    if lives == 0:
        print(lives_visual_dict[lives])
        print("__💀__YOU Died. The word was", word )
    else:
        print("You Guessed the word🌈 ", word, "!!")




if __name__ == '__main__':
    function_2_hangman()
