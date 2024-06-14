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

