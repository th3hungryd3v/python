# Function Name:
# Cannot be a reserved keyword (while, for, etc)
# No Spaces
# Must start with a letter or an underscore
"""
Function Syntax:

def function_name(): <== empty parameter list == no arguments
    statement
    statement
    etc..,
"""
def myFn(): 
    print("You have called my function")

def add(x, y): # <== Two parameters == two arguments
    z = x + y
    print(z)

myFn()
add(12, 12)

a = 12
b = 24

add(a, b)