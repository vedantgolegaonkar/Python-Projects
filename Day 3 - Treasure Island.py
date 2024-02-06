print("Welcome to the treasure Island\nYour mission is to find the treasure.")
def treasure_island():

    step1 = input("You are at a crossover road. Where do you want to go? type 'left' or 'right'? ").lower()
    if step1 == "left":
        step2 = input("You have come to an Island. There is no Island in the middle of the lake. Type 'wait' to wait for a boat. type 'swim' to swim across. ").lower()
        if step2 == "wait":
            step3 = input("You have arrived at Island Unharmed. There is a house with three doors. One red, one yellow and one blue. Which one will you choose? ").lower()
            if step3 == "red":
                print("You are burned allover by fire. Game Over")
                print("\n")
            elif step3 == "blue":
                print("You are eaten by beasts. Game Over")
                print("\n")
            elif step3 == "yellow":
                print("Congratulations!! You have won")
                print("\n")
            else:
                print("Game Over")
                print("\n")
        else:
            print("You are attacked by a trout. Game Over")
            print("\n")
    else:
        print("OOps!! You fell into a hole. Game Over")
        print("\n")

while True:
    treasure_island()
    print("\n")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    print("\n")
    if play_again != 'yes':
        print("Goodbye! Thanks for playing. It was good to have you here")
        break
