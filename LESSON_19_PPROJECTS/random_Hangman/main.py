import random
from file_withwords import words



def get_valid_word():

    word = random.choice(words)


    while '_' in word or ' ' in words:


