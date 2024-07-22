# For this "random" (random will randomize the data) , you need to have min 2 files with the texts, if you dont have the time to use your own texts, copy the data from this repo: https://github.com/kying18/beginner-projects/blob/master/sample_madlibs/hp.py (it s a good practice to do it on your own)

# import the text files

from samples_madlibs import hpotter, vw_orlando_extraits
#
# import the random module
#, random is  a module that provides functions for generating random numbers.
# It is similar to math.random() in other programming languages like JavaScript
import random

if __name__ == "__main__":
    m = random.choice([hpotter, vw_orlando_extraits])
    m.madlib()


# When you will run the code in your terminal, it will launch the input questions, i just answered "whatever" for everything


# --- input questions
#Noun: whatever
# Noun: whatever
# Noun: whatever
# Verb: whatever
# Verb: whatever
# Verb: whatever
# Adjective: whatever
# Adjective: whatever
# Adjective: whatever

# output
# whatever donc Orlando avait-il désiré s’élever au-dessus de ses whatever ? Il semblait whatever , impertinent au whatever point de whatever renchérir sur cette œuvre anonyme, sur le labeur de ces mains disparues. Mieux valait partir inconnu, laissant derrière soi une arche, un cellier, un mur où whatever les whatever que whatever comme un météore whatever qui s’évanouit sans poussière.