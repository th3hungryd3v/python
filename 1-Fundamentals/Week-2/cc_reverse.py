def reverse(str): # define a function with str as an argument
    return str [::-1] # take the str argument and return it  with the extended slice syntax [::-1] <== Extended slice syntax


name = input("What is your name? ")
print("Your name reversed is: ", reverse(name))

# Reversing a string input using a custom_function
#Extended slice syntax == Extended slice offers to put a “step” field as [start,stop,step], and giving no 
# field as start and stop indicates default to 0 and string length respectively and “-1” denotes starting from end and stop at the start, hence reversing string.