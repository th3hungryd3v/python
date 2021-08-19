import random

high_score = 0

def dice_game():
    while True:
        global high_score
        print("\nCurrent High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter Choice: ")
        if choice == "2":
            print("Goodbye!")
            break
        elif choice == "1":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            total = die1 + die2
            print("You roll a... ", str(die1))
            print("You roll a... ", str(die2))
            print("\nYou have rolled a total of: ", str(total))
        if total > high_score:
            high_score += total
            print("\nNew high score!")

dice_game()

































# import random

# high_score = 0

# def dice_game():
#     global high_score
#     while True:
#         print("\nCurrent High Score: ", high_score)
#         print("1) Roll Dice")
#         print("2) Leave Game")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             die1 = random.randint(1, 6)
#             die2 = random.randint(1, 6)
#             roll = die1 + die2
#             print("\nYou rolled a... ", die1)
#             print("You rolled a... ", die2)
#             print("\nYou have rolled a total of: ", high_score)
#         elif roll > high_score:
#             high_score += roll + high_score
#             print("\nNew High Score")
#             continue
#         elif choice == "2":
#             exit()
#             break
#         else:
#             print("C'mon, man? It's not that hard. Try again.")
# dice_game()