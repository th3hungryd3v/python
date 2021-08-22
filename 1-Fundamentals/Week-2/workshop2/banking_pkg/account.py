# Task 4: The banking package
def show_balance(balance):
    print("Current Balance: $" + str(balance))


def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    return balance + amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    return balance - amount 

def logout(name):
    print("Goodbye", name)