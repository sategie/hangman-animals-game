#Import random module to select random words
import random
#Import time  module to create a delay at certain points
import time
#Import list of words from words module
from words import word_list

print("HANGMAN: Animals Version")

name = input("Please enter your name: ")
print("loading...")
time.sleep(1)
print(f"Welcome to the Hangman Animals game, {name}!\n")

def random_word():
    """
    This gets a random word from the list of words
    """
    word = random.choice(word_list)
    return word

random_word()

