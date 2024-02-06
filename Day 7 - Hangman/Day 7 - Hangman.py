# Import the modules
import os
import random
from hangman_words import word_list
from hangman_stages import stages, logo

# function definition for main code
def hangman():

    # function definition to clear screen
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the Hangman Game.\nYou need to guess the correct word before the man goes hanged")
    print("Here you can start guessing the letters")

    # Initialization
    chosen_word = random.choice(word_list)
    word_len = len(chosen_word)
    lives = 6
    print(logo)

    # Display blanks
    display = []
    for _ in range(word_len):
        display += "_"
    print(display)

    # Loop to continue playing
    end_of_game = False
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")
        

        for position in range(word_len):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        
        clear_screen()

        if guess not in chosen_word:
            print(f"You guessed {guess}, That's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You Lose :( ")
                print(f"the correct word was {chosen_word}")
        
        if lives != 0:
            print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You Win!")

        print(stages[lives])


while True:
    hangman()
    print("\n")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    print("\n")
    if play_again != 'yes':
        print("Goodbye. Thanks for playing. It was good to have you here.")
        break