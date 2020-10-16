# VirtualBank_python
Virtual bank code with basic functions in python.

Virtual Bank Instructions: 

Predetermined variables (set the values however you like but keep the data type the same as currently defined)

userList = [0, 1, 2]                 (the list of customers/users username that uses the virtual bank)

userPass = ['', '', '']              (the list of customers/users password that uses the virtual bank)

balances = [300, 400.44, 500.05]     (the list of customers/users current balance that uses the virtual bank)

adminUsername = ''                   (admin username)

adminPassword = ''                   (admin password)

Create a virtual bank that allow customers to withdraw, deposit, and view their balance.
Like most bank ATMs, we want our virtual bank to keep running for each customer throughout the day.
However, we want to have the ability to shut down our virtual bank for maintenance whenever possible.
We want to make sure that only the administrator can shut down the virtual bank with their own username and password.

Create your own virtual bank that has the following functionalities below:

Important functionalities for our Virtual Bank:

- Each customer/user should have their own account name and account password (like a login).

- Allow the customer/user to retry their log in information if no matching name + password pair is found.

- When the bank is on, print a welcome message to your customer.

- When the bank is off, let the administrator know that it's shutting off.

- Create a menu for each customer that allows them to AT LEAST do the following:

- Deposit n amount of money to their current balance.

- Withdraw n amount of money from their current balance.

- If the withdrawal amount is greater than their balance amount, they should not be allowed to withdraw.

- Check their current balance.

- Exit (or log out) of their bank account.

- The virtual bank should continue running until it is shut down by the administrator.

Your code must have at least 6 func tions that does the following:

1. Prompts customers/users for their account number and password.
2. Shows the bank menu.
3. Allow the customer/user to deposit money.
4. Allow the customer/user to withdraw money.
5. Allow the customer/user to check their balance.
6. Allow the customer/user to exit (log out) of their account.

Additional Features (optional):

- Give your virtual bank a name.

- Make each welcome message personalized for your customer/user.

- Accurate floating point calculation for currency value.

- Give the administrator the ability to add new customers/users.

- You will need to create another function to do this.

Cans and Cannots:

- You CAN change how the predetermined variables are set.

- You CAN create more functions but you CANNOT have less than the 6 required ones.

- You CAN create more menu options for the customer/user but you CANNOT have less than the required 4.
