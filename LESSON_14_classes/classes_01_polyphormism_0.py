# The big boss account class that all the other accounts look up to
# 💸 BOSS
class BankAccountBoss:
    #
    #
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # A special method to represent the account when printed
    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance}"
        # The dollar sign was  used as a symbol to represent the currency, not like in react `${somevariable}`
    #--------------------------------------------