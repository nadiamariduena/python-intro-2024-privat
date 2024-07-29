import random
from words  import words
import string

def function_1(words):
    word = random.choice(words)
    while '_' in word or ' ' in words:
        word = random.choice(words)
    return word.upper()


def function_2():
   word = function_1(words)
   word_letters = set(word)
   alphabet = set(string.ascii_uppercase)
   used_letters = set()


   #-----
   lives = 10

   # --
   while len(word_letters) > 0 and lives > 0:

         # -- message the combien des vies i have
        print('You have', lives,  'lives left and you have used these letters: ', ' '.join(used_letters))
        # --  declare a new var 'word_list, then within an array check if the letter in used_letters, else show underscore for letter in word
        word_list = [letter if letter in used_letters else "_" for letter in word]

        # -- print the word_list with spaces join
        print("CURRENT word", " ".join(word_list))
        # --------



        user_letters = input("GUESS a letter: ").upper()

        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)

            if user_letters in word_letters:
                word_letters.remove(user_letters)

            # else condition to reduce - 1 lives
            # so thsat everytime user tries, he has 1 life less
            else:
                lives = lives - 1
                print("\nYour letter,", user_letters, "is not in the word")


        elif user_letters in used_letters:
            print("You already used this letter, TRY AGAIN")

        else:

            print("WRONG char, try again")


# condition to lives to 0
   if lives == 0:
# print died
      print("YOU DIED")
# print won
   else:

       print("YOU WON")









if __name__ in "__main__":
    function_2()