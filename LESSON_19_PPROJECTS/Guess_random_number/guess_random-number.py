import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    # LOOP
    # you need a loop for the guessing
    while guess != random_number:
      guess = int(input(f"Guess a number between 1 and {x}: "))
        #---
      if guess < random_number:
        print("Sorry, guess again. Too LOW 👎")
      elif guess > random_number:
        print("Sorry, guess again. Too high")



guess(10)