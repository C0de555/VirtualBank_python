# PRE-DEFINING VARIABLES AND LISTS
# usernames
user_list = ["user", "person", "someone"]
# passwords
user_pass = ['password!', 'pass', 'word']
# balances
balances = [300, 400.44, 500.05]
# admin username and password
admin_username = "admin"
admin_password = "coding2020"

# FUNCTIONS
def get_valid_username_and_password():
    # Asking for username and password
    global username
    global password

    username = input("Please enter your username to begin: ")
    password = input("Please enter your password: ")

    # if the admin logs on shut down virtual bank
    if username == admin_username and password == admin_password:
        print("Shutting down virtual bank...")
        exit()

    # Getting a valid username and password from user
    # check to see if the username and password are correct on the first time
    user_authenticated = False
    if user_authenticated == False:
        for i in range(3):
            if username == user_list[i]:
                if password == user_pass[i]:
                    user_authenticated = True
                    current_balance = balances[i]
                    break
    while user_authenticated == False:
        # print the error message and allow the user to retype their username and password
        print("Error: username or password was incorrect. Please try again.\n")
        username = input("Please enter your username to begin: ")
        password = input("Please enter your password: ")
        for i in range(3):
            # check if the username and password are valid
            if username == user_list[i]:
                if password == user_pass[i]:
                    # end the loop if the username and password are valid
                    user_authenticated = True
                    break

def bank_menu():
    # print the contents of the bank menu
    print("Type 'd' to deposit money")

    print("Type 'w' to withdraw money")
 print("Type 'c' to check your current balance")
    print("Type 'e' to exit (log out of) your account")
    global user_input
    # ask the user for input
    user_input = input("")


def deposit():
    # define current_balance
    for i in range(3): # change to len(user_list)
        if user_list[i] == username:
            current_balance = balances[i]

    # ask the user how much they would like to deposit
    amount_to_deposit = float(input("How much money would you like to deposit? "))
    # add that amount to the current balance
    current_balance += amount_to_deposit
    # Change the value of the original balance to the value of current balance
    balances[i] = current_balance
    # print a success message
    print("$" + str(amount_to_deposit) + " has successfully been deposited into your account")
    bank_menu()

def withdraw():
    # define current_balance
    for i in range(3):
        if user_list[i] == username:
            current_balance = balances[i]

    # ask the user how much money they would like to withdraw from their account
    amount_to_withdraw = float(input("How much money would you like to withdraw? "))

    # check to see if the amount the user wants to withdraw is greater than the current balance
    # if it is, then print an error message and return to the bank menu
    if amount_to_withdraw > current_balance:
        print("ERROR. Please enter a smaller amount of money to withdraw.")
        bank_menu()
    # if the user enters a valid input, withdraw the amount from their current balance
    else:
        # subtract the amount of money the user would like to withdraw from their account
        current_balance -= amount_to_withdraw
        # Change the value of the original balance to the value of current balance
        balances[i] = current_balance
        print("$" + str(amount_to_withdraw) + " has successfully been withdrawn into your account")
        bank_menu()
def check_balance():
    # define current_balance
    for i in range(3):
        if user_list[i] == username:
            current_balance = balances[i]
    print(balances[i])
    bank_menu()

def log_out():
    print("Exiting now...\nThank you for using the virtual bank.")
    get_valid_username_and_password()
    bank_menu()
    bank_functions()

def bank_functions():
    if user_input == 'd':
        deposit()
        bank_functions()
    elif user_input == 'w':
        withdraw()
        bank_functions()
    elif user_input == 'c':
        check_balance()
        bank_functions()
    elif user_input == 'e':
        log_out()
    else:
        print("ERROR")
        bank_menu()
        bank_functions()

# ACTUAL CODE
# Welcome message
print("Welcome to the virtual bank!")
get_valid_username_and_password()
bank_menu()
bank_functions()
