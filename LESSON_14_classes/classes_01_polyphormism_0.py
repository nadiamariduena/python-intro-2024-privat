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
        """ write something here
        """
    #
    # 🔶 METHOD
    def withdraw(self, amount):
        """ write something here
        """
    # ✅ conditional
#
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
    def fee_deduction(self, fee):
        """ write something here
        """
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
        """ write something here
        """
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
        print(account.fee_deduction(10)) # DEDUCT transaction fee for checking account
    elif isinstance(account, SavingAccount):
        print(account.add_interest(3)) # Add interest for savings account
    elif isinstance(account, InvestmentAccount):
        print(account.invest(5000)) # Invest money in stocks for investment account