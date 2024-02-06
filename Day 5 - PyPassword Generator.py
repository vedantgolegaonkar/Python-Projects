import random

print("Welcome to the PyPassword Generator!")

def password_generator():

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','@','#','$','%','&','*','(',')','+']

    letters_f = int(input("How many letters would you like in your password?\n "))
    symbols_f = int(input("Hpw many symbols would you like?\n "))
    numbers_f = int(input("How many numbers would you like?\n "))

    # Easy Level
    # password = ""

    # for char in range (1, letters_f + 1):
    #     password += random.choice(letters)

    # for char in range(1, symbols_f+1):
    #     password += random.choice(symbols)

    # for char in range(1, numbers_f+1):
    #     password += random.choice(numbers)

    # print(f"Your Password is {password}"")


    # Hard Level

    password_list = []

    for char in range (1, letters_f + 1):
        password_list += random.choice(letters)

    for char in range(1, symbols_f+1):
        password_list += random.choice(symbols)

    for char in range(1, numbers_f+1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char

    print(f"Your password is {password}")


while True:
    password_generator()
    print("\n")
    play_again = input("Do you want to generate another number? (yes/no) : ").lower()
    print("\n")
    if play_again != 'yes':
        print("Goodbye! Thanks for using PyPassword Generator. Hope your account stays protected.")
        break