#
 # 🟠 2 step
class BalanceException(Exception):
    pass

#
# ----------
 # 🟠 1 step
 #parent class
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
        self.getBalance() # coming from line 17
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
            self.getBalance() # coming from line 17
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
             # This line calls a method named withdraw (defined on line 45 , step 4.
             #Purpose: It deducts the amount from the balance of the account from which the transfer is being initiated. This operation simulates the withdrawal of funds from the sender's account to facilitate the transfer.
             #
             #
             self.withdraw(amount)
             #
             # This line calls a method named deposit on the account object.add()#Purpose: It adds the amount to the balance of the account object provided as account. This operation simulates depositing funds into another account, which is the recipient of the transfer.
             account.deposit(amount)
             print("\nTransfer COMPLETE!! ✅")
             #
             #
         except BalanceException as error:
             print(f"\nTransfer interrupted ❌ {error}")

             # 🟠step 7 go to the bank_acc_1_.py




    # inherited data from the above class
    # child of the  "bank_account" in step 1
    # this is a superclass

     # 🟠 step 8:  INTEREST REWARD
     # class method that is responsible for adding an amount including a 5% increase to self.balance
class InterestRewardsAccount(bank_account):
    def deposit(self, amount):
        # self.balance = self.balance + amount # if you use the "amount" positioned at the end of the line, you wont have the possibility to tell it how much you want it to be, like 5% for example
        self.balance = self.balance + (amount * 1.05) # 1.05 which is the 5% | amount * 1.05 calculates 105% of amount, which is amount plus 5% of amount.
        # So you are not just adding the amount like in line 93, but you are adding an additional 5 percent
        print("\nDeposit COMPLETE 🎁")
        self.getBalance()  # coming from line 17



         # 🟠step 9 go to the bank_acc_1_.py , there create an new client with a new account
  #
  #
  #
  #

  # 🟠step 10
  # child of the superclass:   "InterestRewardsAccount" the one above
  #
  ##

  # Savings ACCOUNT
  # #(any withdrawal will have a 5 dollar FEE)

    class SavingsAccount(InterestRewardsAccount):
       def __init__(self, initialAmount, accountName):
          super().__init__(initialAmount, accountName)
          # new property self.fee
          self.fee = 5 # 5 dollar fee for any withdrawal from this account
       def withdraw(self, amount):
           try:
               self.viableTransaction(amount + self.fee)

               #Calls the method viableTransaction (line 33 , step 3) to check if the total transaction amount (including a fee) is viable (i.e., within limits or conditions set by the method).
               #
               #
               self.balance = self.balance - (amount + self.fee)
               #
               # If the transaction is viable, subtracts the total amount (including fee) from the account's balance.
               #
               print("\nWithdraw completed.")
               self.getBalance()
           except BalanceException as error:
               print(f"\nWithdraw interrupted: {error}")

