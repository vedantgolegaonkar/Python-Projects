print("\n")
print("Welcome to the game of Rock Paper and Scissors")
def play_game():

    import random

    rock = '''
        _______
    ---'   ____)
         (_____)
         (_____)
         (____)
    ---._(___)
    '''

    paper = '''
        ________
    ___'    ____)____
                _____)
                _____)
                _____)
            _____)

    '''
    scissors = '''
        _______
    ---'  _____)_____
            _________)
            ________)
          (_____)
    ---.__(____)
    '''

    game_images = [rock, paper, scissors]

    user_choice = int(input("What would you choose? type '0' for Rock, '1' for Paper and '2' for Scissors\n"))

    if user_choice >= 3 or user_choice < 0:
        print("You chose a number greater than 3. You Lose :( ")
    else:
        print("You Choose: ")
        print(game_images[user_choice])

        computer_choice = random.randint(0,2)
        print("Computer Choose: ")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You Win!!!")

        elif computer_choice == 0 and user_choice == 2:
            print("You Lose :( ")

        elif user_choice > computer_choice:
            print("You Win!!!")

        elif computer_choice > user_choice:
            print("You Lose :( ")

        elif user_choice == computer_choice:
            print("It's a draw.")

        else:
            print("Please check the input. You must have provided the wrong number")


while True:
    play_game()
    print("\n")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    print("\n")
    if play_again != 'yes':
        print("Goodbye! Thanks for playing. It was good to have you here")
        break
