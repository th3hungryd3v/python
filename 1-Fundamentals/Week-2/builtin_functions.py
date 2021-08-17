print("Math Functions")

# The abs() function takes a numeric (integer or float) argument and returns its absolute value. 
abs_int = abs(-1)
print(abs_int)

# The float() function takes a numeric argument, converts it to a floating point value, and returns it.
int_to_float = float(100)
print(int_to_float)

# The int() function takes a numeric argument, converts it to an integer value, and returns it
float_to_int = int(1.23)
print(float_to_int)

# You can also use a function inside of print() without having to tie a variable to it first.

print(int(1.23))

# The max() function takes a whole bunch of numeric arguments, and returns the largest one.
print(max(1, 2, -5, 10, 0))

# The min() function takes a whole bunch of numeric arguments, and returns the smallest one.
print(min(1, 2, -5, 10, 0))

# The pow() function takes 2 numbers as an argument, the number on the left is the base number and the second one is the power to multiply by.
print(pow(2, 3)) # 2 to the power of 3

# The round() function takes a floating value and rounds it to the nearest integer.
print(round(51.6))