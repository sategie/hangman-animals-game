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
    Gets a random word from the list of words.
    """
    word = random.choice(word_list)
    return word

def print_remaining_lives(lives, used_letters):
    """
    Prints out a message showing how many lives the user has left.
    Prints out a list of letters already guessed by the user.
    """
    print(f"{lives} lives left. You have used these letters: {sorted([letter for letter in used_letters])}"
  )

def print_current_word(word, used_letters):
    """
    Checks if letter is in the used_letters set.
    Prints out the letter if it is in the set.
    Prints a dash if not
    """
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print(f"Current word: {' '.join(word_list)}")

def get_user_guess(used_letters):
    """
    Checks if the entered letter is valid
    """
    while True:
        user_letter = input("Guess a letter: ")
        if len(user_letter) != 1:
            print("\nPlease enter a single letter.")
        elif user_letter in used_letters:
            print("\nYou have already guessed that letter. Please try another letter.")
        elif not user_letter.isalpha():
            print("\nThat is not a letter. Please enter a letter.")
        else:
            return user_letter.lower()


def check_guess(user_guess, word_letters):
    """
    Check if a user's guess is correct or not
    Update the word_letters set variable accordingly
    """
    if user_guess in word_letters:
        word_letters.remove(user_guess)
        print("")
        return True
    else:
        return False


def play_hangman(name):
    """
    Main hangman function under which all other functions are called
    """
    print_loading()
    print_welcome(name)

    #Create a new hangman game with the defined variables and code each time a new game is started
    while True:
        word = random_word(word_list)
        word_letters = set(word)
        used_letters = set()
        lives = 10
        #Code in this while loop executes if lives are still left and if there are still letters in the word_letters set
        while lives > 0 and word_letters:
            print_remaining_lives(lives, used_letters)
            print_current_word(word, used_letters)
            user_guess = get_user_guess(used_letters)
            used_letters.add(user_guess)
            if not check_guess(user_guess, word_letters):
                lives -= 1
                print(f"\nYour letter, {user_guess}, is not in the word.")

        #Code to display a message if there are no more lives left
        if lives == 0:
            print("Determining your fate...")
            time.sleep(2)
            print(f"Sorry, you got hanged :( The word was {word}.")
        #Code to display a message if the user guessed the word correctly
        else:  
            print(f"Great job {name}! You guessed the correct word: {word}.")


#Check if module is run as the main program and run the function
if __name__ == "__main__":
  name = input("Please enter your name: ")
  play_hangman(name)






