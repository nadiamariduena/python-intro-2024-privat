#
# 2 step
#
class BalanceEception(Exception):
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

        # 3 step
    def viableTransaction(self, amount):
        if self.balance >= amount:
             return
        else:
            raise BalanceEception(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}" # or INSUFFICIENT fonds
            )