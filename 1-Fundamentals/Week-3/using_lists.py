# List
states = ["Washington", "Oregon", "California"]

""" 
print(states[-1])
print(states[-2])
print(states[-3])

"""
states[2] = "Arizona"

# print(states)

# print(len(states))

# Methods are like functions:
# - Used to run pre-defined code
# - Can be built-in or custom
# - Called by name, followed by argument list in parentheses
# Unlike functions, methods are always associated with an object
# - A list is a type of object (list object)
# There are specific built-in methods for lists
# Use dot notation: listname.methodname(arguments)
# ex. states.append("New York")
# append() will append(add) whatever the argument is to the list object
states.append("New York")
print(states)
# pop() will remove the last item in the list object without any arguments, but adding an index number as an argument will remove the object, in the list, from that index.
states.pop()
print(states)

states.pop(1)
print(states)