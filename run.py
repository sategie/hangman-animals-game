#Import random module to select random words
import random
#Import time  module to create a delay at certain points
import time
#Import list of words from words module
from words import word_list

print("HANGMAN: Animals Version")
print("........................")

def print_welcome(name):
    """
    Function to display a welcome message after the user enters a name
    """
    print(f"Welcome to the Hangman Animals game, {name}!\n")

def print_loading():
    """
    Function to display the loading sign before the game starts
    """
    print("loading...")
    time.sleep(1)

def random_word(word_list):
    """
    This gets a random word from the list of words
    """
    word = random.choice(word_list)
    return word

def play_hangman(name):
    print_loading()
    print_welcome(name)

#Check if module is run as the main program and run the function
if __name__ == "__main__":
  name = input("Please enter your name: ")
  play_hangman(name)


