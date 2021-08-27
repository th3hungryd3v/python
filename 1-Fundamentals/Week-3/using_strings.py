my_string = "alpha"
# You'll notice that even though it's a multiline string, it will print it out without regards to the spacing
'''multiline_string = """bravo
charlie"""

print(my_string)
print(multiline_string)'''

# retrieve a single character by index using bracket notation
'''print(my_string[0])
print(my_string[3])'''

# The first three lines show the different ways you can use slice notation with a string to get substrings
print(my_string[0:3])
print(my_string[:2])
print(my_string[2:])
# And this last line shows that the original string is not manipulated in any way, my_string is still == "alpha"
print(my_string)

# if you try to change the string in any way it will cause an error because strings are an immutable data type.

# my_string[0] = "b"

# Iterate through a string using for

'''for char in my_string:
    print(char)
'''
# Finding whether a substring exists in a string

print("pha" in my_string)
print("z" in my_string)
