import random
import os
from art import logo

easy_level_attempt = 10
hard_level_attempt = 5

def check_number(number, guess, attempts):
    if guess > number:
        print("You guessed too high.")
        return attempts -1
    elif guess < number:
        print("You guessed too low.")
        return attempts - 1
    else:
        print("Congratulations! You got it")

def set_difficulty():
    level = input("Select your difficulty level. 'easy' or 'hard'?: ").lower()
    if level == "easy":
        return easy_level_attempt
    else:
        return hard_level_attempt

def game():
    os.system("cls")
    print(logo)
    print("Welcome tho the Number Guessing Game")
    print("I am guessing a number between 1 and 100")

    number = random.randint(1,100)
    attempts = set_difficulty()

    guess = 0
    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.\n")
        guess = int(input("Guess the number in my mind: "))
        os.system("cls")
        attempts = check_number(number=number, guess=guess, attempts=attempts)
        if attempts == 0:
            print("You ran out of all your attempts. You lose")
            print(f"The number was {number}")
            break
        elif guess != number:
            print("Guess again.\n")


while True:
    game()
    print("\n")
    play_again = input("Do ypu want to challenge again? (y/n): ").lower()
    if play_again !="y":
        os.system("cls")
        print("Thanks for Playing")
        break