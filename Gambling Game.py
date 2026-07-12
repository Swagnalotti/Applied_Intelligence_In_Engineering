import random

money = 5
play_again = "Y"
range = 10

while money > 0 and (play_again == "Y" or play_again == "y"):
    dealer_number = random.randint(0, range)
    player_number = int(input(f"Enter a number between 0 and {range}: "))

    if player_number == dealer_number:
        money = money + 2 * range / 10
        range = range + 10
        print(f"You Win! You have ${money} 🤑🤑🤑")
    else:
        money = money - 1
        print(f"You Lose! You have ${money} 😔😔😔")

    play_again = input("Enter Y/y to play again: ")