from bank_accounts_0 import *
#
#

Dave = bank_account(1000, "Dave")
Sara = bank_account(2000, "Sara")

# Call the second method
print("--- BALANCE  ----")
Dave.getBalance()
Sara.getBalance()

# 🤚 result
# Account 'Dave' balance = $1000.00
# Account 'Sara' balance = $2000.00
print("")
print("--- DEPOSIT  ----")
Sara.deposit(500)
# result
# As you can see, it added 500 to the 2000 (Sara s BALANCE)
#Account 'Sara' balance = $2500.00
#
#
print("")
print("--- WITHDRAW  ----")
# ** WITHDRAW
Dave.withdraw(10000)
# result
#Withdraw interrupted:
# Sorry, account 'Dave' only has a balance of $1000.00
#
#
# now with Sara (she has 2000)
Sara.withdraw(1500)
# result
#Withdraw complete.
# Account 'Sara' balance = $1000.00
print("")
print("--- TRANSFER  ----")
# ** TRANSFER
# transfer amount to Saras account
Dave.transfer(25400, Sara)
#
# RESULT
# Since Dave doesnt have such amount, you will get an exception
#-----------
#Beginning Transfer.. 🚀
# Transfer interrupted ❌
# Sorry, account 'Dave' only has a balance of $1000.00
#
print("")
print("--- new TRANSFER  ----")
# TRy AGAIN, this time just an small amount
Dave.transfer(400, Sara)

## result

# --- new TRANSFER  ----

# *******

# Beginning Transfer.. 🚀

# Withdraw complete.

# Account 'Dave' balance = $600.00

# Deposit complete.

# Account 'Sara' balance = $1400.00

# Transfer COMPLETE!! ✅

print("")
print("--- INTEREST REWARD  ----")

Jim = InterestRewardsAccount(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

# RESULT

# --- INTEREST REWARD  ----

# Account 'Jim' created.
# Balance = $1000.00

# Account 'Jim' balance = $1000.00

# Deposit COMPLETE 🎁

#✋ the reward with the 5%
# Account 'Jim' balance = $1105.00