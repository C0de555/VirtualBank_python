# Predetermined variables (set the values however you like but keep the data type the same as currently defined)
# userList = [0, 1, 2]                # the list of customers/users username that uses the virtual bank
# userPass = ['', '', '']             # the list of customers/users password that uses the virtual bank
# balances = [300, 400.44, 500.05]    # the list of customers/users current balance that uses the virtual bank
# adminUsername = ''                  # admin username
# adminPassword = ''                  # admin password

# Create a virtual bank that allow customers to withdraw, deposit, and view their balance.
# Like most bank ATMs, we want our virtual bank to keep running for each customer throughout the day.
# However, we want to have the ability to shut down our virtual bank for maintenance whenever possible.
# We want to make sure that only the administrator can shut down the virtual bank with their own username and password.
# Create your own virtual bank that has the following functionalities below:

# Important functionalities for our Virtual Bank:
    # Each customer/user should have their own account name and account password (like a login).
        # Allow the customer/user to retry their log in information if no matching name + password pair is found.
    # When the bank is on, print a welcome message to your customer.
    # When the bank is off, let the administrator know that it's shutting off.
    # Create a menu for each customer that allows them to AT LEAST do the following:
        # Deposit n amount of money to their current balance.
        # Withdraw n amount of money from their current balance.
            # If the withdrawal amount is greater than their balance amount, they should not be allowed to withdraw.
        # Check their current balance.
        # Exit (or log out) of their bank account.
    # The virtual bank should continue running until it is shut down by the administrator.
    # Your code must have at least 6 functions that does the following:
        # 1. Prompts customers/users for their account number and password.
        # 2. Shows the bank menu.
        # 3. Allow the customer/user to deposit money.
        # 4. Allow the customer/user to withdraw money.
        # 5. Allow the customer/user to check their balance.
        # 6. Allow the customer/user to exit (log out) of their account.

# Additional Features (optional):
    # Give your virtual bank a name.
    # Make each welcome message personalized for your customer/user.
    # Accurate floating point calculation for currency value.
    # Give the administrator the ability to add new customers/users.
        # You will need to create another function to do this.

# Cans and Cannots:
    # You CAN change how the predetermined variables are set but you CANNOT change the preset data types.
        # Ex: userList must always be a list of ints, balances must always be a list of floats, etc.
    # You CAN create more functions but you CANNOT have less than the 6 required ones.
    # You CAN create more menu options for the customer/user but you CANNOT have less than the required 4.

# Additional Notes:
    # When testing your virtual bank, test all use case you can think of.
        # The point is to see if you can break your code.
    # Work on finishing the base functionality first before trying to implement the additional features that seem
    # more complicated.

# ---------------------------------------------------------------------------------------------------------------
# You can start your code here:

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
        for i in range(len(user_list)):
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
        for i in range(len(user_list)):
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
    for i in range(len(user_list)):
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
    for i in range(len(user_list)):
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
    for i in range(len(user_list)):
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
