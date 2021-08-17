# Type Casting (Type Conversion)
# Python does not perform automatic type conversion, so you must do it yourself.

# str(arg) | Argument passed in will be returned as a String
# int(arg) | Argument passed in will be returned as an Integer
# float(arg) | Argunment passed in will be returned as a Float, Argument must contain a number though.
# float() can take both an integer and float argument

total_cash = 0
user_input = input("Enter amount to transfer: ")
total_cash = total_cash + float(user_input)

print("Total cash is now: ")
print(total_cash)