import random

print("Welcome to the Slot Machine")

INIT_STAKE = 50
ITEMS = ["🍒", "🍋", "🍊", "🍑", "🔔", "🍫"]

first_wheel = None
second_wheel = None
third_wheel = None
stake = INIT_STAKE

def spin_wheel():
    random_number = random.randint(0, 5)
    return ITEMS[random_number]

def play():
    global stake, first_wheel, second_wheel, third_wheel

    play_question = ask_player()

    while stake != 0 and play_question == True:
        first_wheel = spin_wheel()
        second_wheel = spin_wheel()
        third_wheel = spin_wheel()
        print_score()
        play_question = ask_player()

def ask_player():
    global stake
    while True:
        answer = input(f"You have ${stake}. Would you like to play? ")
        answer = answer.lower()

        if answer == "yes" or answer == "y":
            return True

        elif answer == "no" or answer == "n":
            print(f"You ended the game with ${stake} in your hand.")
            return False

        else:
            print("wrong input!")

def print_score():
    global stake, first_wheel, second_wheel, third_wheel
    if first_wheel == "CHEERY" and second_wheel != "🍒":
        win = 2
    elif first_wheel == "🍒" and second_wheel == "🍒" and third_wheel != "🍒":
        win = 5
    elif first_wheel == "CHEERY" and second_wheel == "🍒" and third_wheel == "🍒":
        win = 7
    elif first_wheel == "🍊" and second_wheel == "🍊" and (third_wheel == "🍊" or third_wheel) == "🍫":
        win = 10
    elif first_wheel == "🍑" and second_wheel == "🍑" and (third_wheel == "🍑" or third_wheel) == "🍫":
        win = 14
    elif first_wheel == "🔔" and second_wheel == "🔔" and (third_wheel == "🔔" or third_wheel) == "🍫":
        win = 20
    elif first_wheel == "🍫" and second_wheel == "🍫" and third_wheel == "🍫":
        win = 250
    else:
        win = -1

    stake += win
    if win > 0:
        print(f"{first_wheel} \t\t {second_wheel} \t {third_wheel} -- You win ${win}")
    else:
        print(f"{first_wheel} \t\t {second_wheel} \t {third_wheel} -- You lose")

play()