#
 # 🟠 2 step
class BalanceException(Exception):
    pass

#
#
 # 🟠 1 step
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
    # 🟠 3 step
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
     # 🟠 4 step
     # Use the Try to catch "error or exception" (so if something wrong happens in step 3, the below code will catch it)
     #

    def withdraw(self, amount):
        try:
            #This line calls a method named viableTransaction that is defined in line 32 (step 3)
            self.viableTransaction(amount)
            #
            #
            #This line subtracts the amount from the current balance (self.balance) of the account.
            #Purpose: It updates the balance after a successful withdrawal. For instance, if you have $100 in your account and you withdraw $20, this operation updates the balance to $80.
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
            # Calls the getBalance() , Display the updated balance after the withdrawal.
            #Purpose: It updates the display of the current balance after the withdrawal operation. This helps in showing the user the updated amount of money left in their account after the withdrawal.
            #
            # remember: to use this exception you need to declare it first (check step 2)
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

            # 🟠step 5 go to the bank_acc_1_.py

     # 🟠 step 6
    def transfer(self, amount, account):
         try:
             print("\n*******\n\nBeginning Transfer.. 🚀 ")
             #
             # Purpose: Similar to the previous explanation, it checks if the transfer of amount is possible or allowed based on certain conditions. For instance, it might verify if the account initiating the transfer has sufficient funds.

             self.viableTransaction(amount)
             self.withdraw(amount)
             account.deposit(amount)
             print("\nTransfer COMPLETE!! ✅")

