# Task 4: The banking package
def show_balance(balance):
    print(float(balance))

def deposit(balance):
    amount = input("Enter the amount to deposit: ")
    return balance + float(amount)

def withdraw(balance):
    amount = input("Enter the amount to withdraw: ")
    return float(amount) - balance

def logout(name):
    print("Goodbye", name)