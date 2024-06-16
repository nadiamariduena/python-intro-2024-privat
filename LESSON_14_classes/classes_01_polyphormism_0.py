# The big boss account class that all the other accounts look up to
# 💸 BOSS
class BankAccountBoss:
    #
    #
    def __init__(self, account_number, balance):
        #
        self.account_number = account_number
        self.balance = balance

    # A special method to represent the account when printed
    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance}"
        # The dollar sign was  used as a symbol to represent the currency, not like in react `${somevariable}`
    #--------------------------------------------
    #
    #
    # 🔶 METHOD
    def deposit(self, amount):
        """
        Deposits the given amount into the acount.

        Parameters:
        - amount (float): The amount to be deposited.

        Returns:
        - str: A message indicating the deposit and the new balance.
        """

        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance} 💸 "
    #
    # 🔶 METHOD
    # a method to withdraw money from the account
    def withdraw(self, amount):
        """
        Withdraws the given amount from the account if sufficient balance is available.

        Parameters:
        - amount (float): The amount to be withdrawn.

        Returns:
        - str: A message inidcating the withdrawal and the new balance if successful, or an "Insufficient funds!" message if the balance is insufficient.
        """
    # ✅ conditional

        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance} 🍊"
        else:
            return "Insufficient funds"


#
#
# --------------
# 🟣 Checking ACCOUNT: A basic account for day to day transactions
# --------------
class CheckingAccount(BankAccountBoss):
    def __init__(self, account_number, balance):
        # Calls the constructor of the bank account
        super().__init__(account_number, balance)

    #
    # 🔶 METHOD
    # A special method only for Checking Account
    def fee_deduction(self, fee):
        """
        Deducts a transaction fee from the account balance.

        Parameters:
        - fee (float): The transaction fee amount to be deducted.

        Returns:
        - str: A message indicating the deduction and the new balance.
        """

        self.balance -= fee
        return f"Deducted ${fee} as a transaction fee. New balance: ${self.balance} 🌻"

        # --------------
#
#
#
# --------------
# 🟣 Savings Account: An account for saving money and earning interest
# --------------
class SavingAccount(BankAccountBoss):
    def __init__(self, account_number, balance):
        # Calls the constructor of the bank account
        super().__init__(account_number, balance)

         # 🔶 METHOD
    def add_interest(self, interest_rate):
        """
        Adds interest to the account balance based on the given interest rate.

        Parameters:
        - interest_rate (float): The interest rate (in percentage) to be applied.

        Returns:
        - str: A message indicating the interest added and the new balance.
        """

        interest = self.balance * (interest_rate / 100 )
        self.balance += interest
        return f" Added interest of ${interest}. NEW balance: ${self.balance}  "

        # --------------

#
#
#
# --------------
# 🟣  Investment Account: An account for investing money in stocks and bonds
# --------------
class InvestmentAccount(BankAccountBoss):
    def __init__(self, account_number, balance):
        # Calls the constructor of the bank account
        super().__init__(account_number, balance)

    def invest(self, investment_amount):
        """
        Invest ...
        """


# Our  banking   lineup with different types of accounts

accounts = [
    CheckingAccount("123456", 1000), # Checking Account
    SavingAccount("789012", 5000), #Savings Account
    InvestmentAccount("345678", 20000) # Investment Account

]

# Lets manage some money matters!
for account in accounts:
    #let's see what kind of account we're dealing with
    print(account)
    #
    #
    # Now, let's perform some banking weÄre dealing with
    if isinstance(account, CheckingAccount):
        print(account.fee_deduction(10)) # Deduct $10 as a transaction fee for checking account
    elif isinstance(account, SavingAccount):
        print(account.add_interest(3)) # Add 3% interest for savings account
    elif isinstance(account, InvestmentAccount):
        print(account.invest(5000)) # Invest $5000 in stocks for investment account
    print()

    # 🖐️ OUTPUT

#     Account Number: 123456, Balance: $1000
# None

# Account Number: 789012, Balance: $5000
# None

# Account Number: 345678, Balance: $20000
# None

