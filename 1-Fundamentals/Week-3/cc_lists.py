import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    choice = input("Press enter to pick a card, any card! or press Q + enter to quit. ")
    if choice == "Q" or choice == "q":
        break
    else:
        card = random.choice(diamonds)
        diamonds.remove(card)
        hand.append(card)
        print("Your hand:", str(hand))
        print("Remaining cards:", str(diamonds))

if not diamonds:
    print("There are no more cards to pick.")

