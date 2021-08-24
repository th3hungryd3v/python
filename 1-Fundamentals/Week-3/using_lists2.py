# List
states = ["Washington", "Oregon", "California"]
# iterating through a list using for
'''for x in states:
    print(x)'''
# Can also be written like so:
# for state in states:
# Make state all lower-case before we print it
    # state = state.lower()
    # print(state)
# Another way to use the in keyword
# print("Washington" in states) # Although there is no way to run custom code through each loop iteration

states2 = ["Arizona", "Ohio", "Louisiana"]
# Concatenation
best_states = states + states2
print(best_states)
print(best_states[1:3]) # Starting from index 1 to 3, but not including 3
print(best_states[:2]) # Only up to index 2, but not including 2
print(best_states[4:]) # Start from index 4 all the way to the end.


