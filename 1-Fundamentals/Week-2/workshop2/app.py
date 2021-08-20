def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
# Task 2: Registration
print("          === Automated Teller Machine ===          ")
user = input("Enter name to register: ")
pin = input("Enter Pin: ")
balance = 0
print(user, "has been registered with a starting balance of $" + str(balance))

# Task 3: Login and prompt for menu option
