from bank_accounts_0 import *

Dave = bank_account(1000, "Dave")
Sara = bank_account(2000, "Sara")

# Call the second method
Dave.getBalance()
Sara.getBalance()

# 🤚 result
# Account 'Dave' balance = $1000.00
# Account 'Sara' balance = $2000.00

Sara.deposit(500)
# result
# As you can see, it added 500 to the 2000 (Sara s BALANCE)
#Account 'Sara' balance = $2500.00
#
#

Dave.withdraw(10000)
# result
#Withdraw interrupted:
# Sorry, account 'Dave' only has a balance of $1000.00
#
#
# now with Sara (she has 2000)
Sara.withdraw(1500)