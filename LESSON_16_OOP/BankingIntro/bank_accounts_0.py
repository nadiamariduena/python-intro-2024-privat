#
# 2 step
class BalanceException(Exception):
    pass

#
#
# 1 step
class bank_account:
    def __init__(self, initialAmount, accountName):

        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        # remember: the :.2 will format the balance outcome to a 2 decimal points, so it will represent the cents

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()
    #
    #
    #
    # 3 step
    # check if the user has sufficient funds
    # check some examples here: https://www.smscountry.com/blog/sms-templates-for-financial-services/
    #
    #
    def viableTransaction(self, amount):
        if self.balance >= amount:
             return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}" # or INSUFFICIENT funds
            )
     #
     #
     # 4 step
     # Use the Try to catch "error or exception" (so if something wrong happens in step 3, the below code will catch it)
     #

    def withdraw(self, amount):
        try:
            #This line calls a method named viableTransaction that is defined in line 32 (step 3)
            self.viableTransaction(amount)
            #This line subtracts the amount from the current balance (self.balance) of the account.

            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
            #
            # remember: to use this exception you need to declare it first (check step 2)
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
