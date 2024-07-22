# Mad Libs is a word game created by Leonard Stern and Roger Price. It consists of one player prompting others for a list of words to substitute for blanks in a story before reading aloud


#🟡
# string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to ____"
youtuber = "Dorothea Ernst" # some string variable


# # a few ways to do this
print("subscribe to " + youtuber)
print("subscribe to {}". format(youtuber))
print(f"subscribe to {youtuber}")

# subscribe to Dorothea Ernst
# subscribe to Dorothea Ernst
# subscribe to Dorothea Ernst


# ---------------------------

print("---- 🍀 ----")

adj = input("Adjetive: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \ I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person} "


print(madlib)