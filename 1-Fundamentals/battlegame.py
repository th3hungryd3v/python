# Global Character and Stat Variables
# Task 1 - Set up your game variables: the game characters and their stats.
wizard = "Wizard"
elf = "Elf"
human = "Human"
wizard_hp = 70
elf_hp = 100
human_hp = 150
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_hp = 300
dragon_damage = 50

# Task 2 + Task 3 - Prompt the player to choose from a list of options. + set up infinite loop to handle player choice.
while True:
    print("1)   Wizard")
    print("2)   Elf")
    print("3)   Human")
    character = int(input("Choose your character: "))
    if character == 1:
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("You have chosen the character: " + character)
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        break
    elif character == 2:
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("You have chosen the character: " + character)
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        break
    elif character == 3:
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("You have chosen the character: " + character)
        print("Health: " + str(my_hp))
        print("Damage: " + str(my_damage))
        break
    else:
        print("Unknown character")
# Task 4 - Battle with the Dragon!
while True:
    dragon_hp = dragon_hp - my_damage
    print("The " + character + " damaged the Dragon!")
    print("The Dragon's hitpoints are now: " + str(dragon_hp))
    if dragon_hp == 0:
        print("The Dragon has lost the battle")
        break
