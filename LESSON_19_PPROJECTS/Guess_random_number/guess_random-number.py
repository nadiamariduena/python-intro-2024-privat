import random  # Step 1: Importing the 'random' module for generating random numbers

def guess(x):
    #random_number: This variable holds the randomly generated integer, which remains constant throughout the program execution until the user correctly guesses it.
    random_number = random.randint(1, x)  # Step 2: Generating a random number between 1 and 'x'
    #    # random.randint(1, x): This function call from the random module generates a random integer. The parameters 1 and x specify the range within which the random number can fall. Here, 1 ensures the random number starts from the lowest possible value (which is 1), and x is the upper limit.

    #
    guess = 0  # Step 3: Initializing the 'guess' variable to 0

    # Step 4: Loop for guessing the number
    while guess != random_number:
        #This line prompts the user to "input" their guess and converts that input into an integer.
        guess = int(input(f"Guess a number between 1 and {x}: "))  # Step 5: Taking user input for a guess


        # Step 6: Checking if the guess is too low, too high, or correct
        if guess < random_number:
            print("Sorry, guess again. Too LOW 👎")  # Step 7a: Providing feedback for a guess that is too low
        elif guess > random_number:
            print("Sorry, guess again. Too high")  # Step 7b: Providing feedback for a guess that is too high

# Step 8: Calling the function with 'x' = 10, allowing guesses between 1 and 10
guess(10)
