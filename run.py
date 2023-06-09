# Import random module to select random words
import random
# Import time  module to create a delay at certain points
import time
# Import list of words from words module
from words import word_list


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


def print_remaining_lives(lives, guessed_letters):
    """
    Takes two parameters:
    lives: integer showing the number of remaining lives
    guessed letters: list of letters already guessed

    Prints out a message showing how many lives the user has left.
    Prints out a list of letters already guessed by the user.

    The sorted method in the print statement sorts out the guessed letters alphabetically
    """
    print(f"{lives} lives left. You have used these letters: {sorted([letter for letter in guessed_letters])}"
  )


def print_current_word(word, guessed_letters):
    """
    Creates a new list 'word_list' using list comprehension which does the following:
    Iterates over each letter in the random word
    Checks if the letter is available in the guessed_letters list
    Adds the letter to word_list if it is available in guessed_letters list.
    Adds a dash to word_list if the letter is not available in the guessed_letters list.
    
    When the iteration is completed, it prints the word_list

    The join method is used to create a single string from the individual elements in word_list
    The empty string with the space ' ' is the delimiter and this creates spacing between the individual letters in the string.
    """
    word_list = [letter if letter in guessed_letters else '-' for letter in word]
    print(f"Current word: {' '.join(word_list)}")


def get_user_guess(guessed_letters):
    """
    Checks if the entered letter is valid.

    Prints messages alerting the user if the guess is invalid.
    Returns the letter in lower case if the guess is valid
    """
    while True:
        user_letter = input("Guess a letter: ").strip()
        if len(user_letter) != 1:
            print(f"\nPlease enter only one letter.")
        elif user_letter in guessed_letters:
            print(f"\n'{user_letter}' has already been used. Please guess another letter.")
        elif not user_letter.isalpha():
            print(f"\n'{user_letter}' is not a letter. Please enter a letter.")
        else:
            return user_letter.lower()


def check_guess(user_guess, unique_letters_word):
    """
    Takes the following parameters:
    user_guess: The letter guessed by the user after validation.
    unique_letters_word: The word set chosen at random from word_list which contains all unique letters in the word.

    Checks if a user's guess is correct or not.
    Updates the unique_letters_word set variable accordingly.

    Returns a boolean:
    True if the guessed letter is in the word set.
    False if the guessed letter is not in the word set
    """
    if user_guess in unique_letters_word:
        unique_letters_word.remove(user_guess)
        print("")
        return True
    else:
        return False


def play_hangman(name):
    """
    Main hangman function under which all other functions are called

    Takes only one parameter: The name of the user

    Each code block is explained using single line comments
    """
    print_loading()
    print_welcome(name)

    # Create a new hangman game with the defined variables and code each time a new game is started
    while True:
        word = random_word(word_list)
        unique_letters_word = set(word)
        guessed_letters = set()
        lives = 6
        #Code in this while loop executes if lives are still left and if there are still letters in the unique_letters_word set
        while lives > 0 and unique_letters_word:
            print_remaining_lives(lives, guessed_letters)
            print_current_word(word, guessed_letters)
            user_guess = get_user_guess(guessed_letters)
            guessed_letters.add(user_guess)
            if not check_guess(user_guess, unique_letters_word):
                lives -= 1
                print(f"\nYour letter, {user_guess}, is not in the word.")

        # Code to display a message if there are no more lives left
        if lives == 0:
            print("Determining your fate...")
            time.sleep(2)
            print(f"Sorry, you got hanged :( The word was {word}.")
        # Code to display a message if the user guessed the word correctly
        else:
            print(f"Great job {name}! You guessed the correct word: {word}.")
        # Code to run depending on if the user decides to play again or not
        play_again = input("Do you want to play again? (y/n) ").lower().strip()

        # Code to validate the y or n entry
        while play_again != 'y' and play_again != 'n':
            print(f"Please enter 'y' or 'n'.")
            play_again = input("Do you want to play again? (y/n)").lower().strip()
        # Code to display if user does not want to play again
        if play_again != "y":
            print(f"Thanks for playing {name}!\n")
            print("HANGMAN: Animals Version")
            print("........................")
            name = input("Please enter your name: ").strip()
            play_hangman(name)
        # Code to display if user wants to play again
        else:
            print(f"\nWelcome back to the Hangman Animals game {name}!\n")

# Check if module is run as the main program and run the function


if __name__ == "__main__":
    print("HANGMAN: Animals Version")
    print("........................")
    # Code to prompt user to enter only letters when entering the name
    while True:
        name = input("Please enter your name: ").strip()
        if name.isalpha():
            play_hangman(name)
        else:
            print("Please enter only letters")