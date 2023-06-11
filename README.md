# Hangman: Animals Game

This project is based on the classic Hangman game in which a user has to guess the letters in an unknown word before the game ends.
Each player has a fixed amount of lives and if the word is not guessed before the number of lives reaches zero, the player gets hanged.

This version uses only animals and gives the user a total of 6 lives to guess the correct animal.

The game was designed using only the Python language, hence it is not accessible in a web browser, but rather in the command line interface (CLI).

![Image of start page of the game in the CLI](/documentation/main-page.png)

## Features

- **Main screen**

    - When the game loads, the user is presented with the title of the game and prompted to enter the name.

    ![Image of start page of the game in the CLI](/documentation/main-page.png)

- **Gameplay**

    - When the user enters the name field, a 'loading...' message appears for 1 second and then a welcome message is displayed to welcome the user.
    - The game begins with 6 lives
    - There is an empty list in which the guessed letters are displayed in alphabetical order.
    - The user is provided with blank lines in which the letters in the current word have to be guessed
    - If a user guesses the wrong letter, a message appears informing the user that the chosen letter is not in the word and the life is reduced by 1.
    - If a user guesses the correct letter in the word, the letter appears in one of the blank lines and the amount of lives do not change.
    - The amount of lives only reduces when the user guesses a new incorrect letter.
    - If the user tries to use one of the letters which has already been guessed, a message appears informing the user that the letter has already been used and the user is then prompted to guess another letter.
    - The game ends if one of the following applies:
        - The user guesses all correct letters before the number of lives is used up.
        - The number of lives is used up .i.e the user has not guessed the correct word in 6 attempts
    - When the game ends, the correct word is displayed and the user is asked if they want to play again or not.
        - If the user chooses to play again, a message appears welcoming the user back to the game.
        - The number of lives resets back to 6 and the letters in a new random word have to be guessed.
        - If a user chooses not to play again, a message appears thanking the user for playing and the game goes back to the main screen and asks the user to enter a name.

![Image showing an example of the actual gameplay](/documentation/gameplay-one.png)

![Image showing an example of the actual gameplay](/documentation/gameplay-two.png)

![Image showing an example of the actual gameplay](/documentation/gameplay-three.png)

![Image showing an example of the actual gameplay](/documentation/gameplay-four.png)

## Technologies Used

- Python: The programming language in which the game is written

- CodeAnywhere: The IDE used for writing the actual Python code.

- Github: This was used for remote storage and version control.

- Heroku: This was used to deploy the project.

- Screenpresso: This was used to make screenshots of the deployed project.

- prettier.io: This was used to arrange each word in the words list in order to make them appear on separate lines




    

