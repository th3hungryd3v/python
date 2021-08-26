import random # import random module

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"] # List of cards

hand = [] # Empty list to append the cards to

while diamonds:
    choice = input("Press enter to pick a card, any card! or press Q + enter to quit. ")
    if choice == "Q" or choice == "q":
        break
    else:
        card = random.choice(diamonds) # Create a variable named cards and give it the random.choice from the diamonds list
        diamonds.remove(card) # remove the card from the diamonds list
        hand.append(card) # add the card that was removed from the diamonds list and put it inside the hand list
        print("Your hand:", str(hand))
        print("Remaining cards:", str(diamonds))

if not diamonds: # When the diamonds list no longer holds any cards, print the following statement and exit.
    print("There are no more cards to pick.")

