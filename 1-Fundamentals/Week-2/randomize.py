import random # import random module

pips = random.randint(1, 6) # Create a variable and give it the value of the module.with an argument of 1 and 6
print("You roll the die... it lands with", pips, "pips showing.") # print a string with the variable seperating them with a ",".
# Using a "," is almost like using a "+" -- But when using a comma it adds a space to your string

prizes = ["a car", "$10000", "a pony", "$500000"] # A list mapped to a variable
prize_won = random.choice(prizes) # A variable mapped to random
print("You turn the wheel of fortune... It lands on a prize of", prize_won + "!!")

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # Another list mapped to a variable
random.shuffle(cards)# Use random with dot notation to "shuffle" the cards list
print("The cards are now in this order: ")
print(cards)