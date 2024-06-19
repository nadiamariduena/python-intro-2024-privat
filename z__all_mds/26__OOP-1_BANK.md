## 🟣 Banking example

 <br>

```python
class bank_account:
# initialAmount and accountName are parameters that you define for the __init__ method.
    def __init__(self, initialAmount, accountName):

        self.balance = initialAmount
        self.name = accountName
```

<br>

#### Question: So i can add whatever i want and, they will represent the initial amount and the account name

##### chatgpt:

> Exactly! In Python (and in many object-oriented programming languages), when you define a class like bank_account, you can specify what attributes (data) each instance of that class should have when it is created. These attributes are initialized using the **init** method, which acts as a constructor for the class.

```python
# keep in mind balance and name arent methods but attributes you will assign tje initial Amount & accountName
  self.balance = initialAmount
        self.name = accountName
```

<br>

### After the below, create another component

- there you will be adding most of the logic

```python
class bank_account:
    def __init__(self, initialAmount, accountName):

        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        # remember: the :.2 will format the balance outcome to a 2 decimal points, so it will represent the cents
```

<br>

> `${self.balance:.2f}` formats the **self.balance** attribute as a floating-point number with two decimal places.

- This is a common way to represent currency or precise numerical values in Python.

<br>

#### Relating to JavaScript:

In JavaScript, a similar concept might be achieved using template literals (backticks), especially when you want to interpolate variables or expressions into a string. Here’s how the equivalent might look in JavaScript:

```javascript
console.log(
  `\nAccount '${this.name}' created.\nBalance = $${this.balance.toFixed(2)}`
);
```

<br>

---

<br>

#### Back to the bank example

- within the file **bank_accounts_0.py** , I have the below code

```python
class bank_account:
    def __init__(self, initialAmount, accountName):

        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        # remember: the :.2 will format the balance outcome to a 2 decimal points, so it will represent the cents
```

<br>

### 🔶 Call it

#### Now within the second file `bank_acc_1_.py`

- I will add the below code to show the account name and balance based on the above code (you will call it here:)

```python
# the *: stands for import ALL
from bank_accounts_0 import *

# ✋Just like when you grab data from a js or json file, you have to insert the name of the class coming from the first file
Dave = bank_account(1000, "Dave")
Sara = bank_account(2000, "Sara")
# print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
```

#### result

```python
Account 'Dave' created.
Balance = $1000.00 # :.2f}

Account 'Sara' created.
Balance = $2000.00 # :.2f}
```

<br>
<br>

#### 🟢 ADD a METHOD

- back to the `bank_acc_1_.py`

- Add a new method, name it `getBalance()`

```python
     def getBalance(self):
            print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
```

<br>

### 🔶 Call it

- Go to the second file `bank_acc_1_.py` , and add the calling

```python
# Call the second method
Dave.getBalance()
Sara.getBalance()

# 🤚 result
# Account 'Dave' balance = $1000.00
# Account 'Sara' balance = $2000.00
```

<br>
<br>

#### 🟢 ADD a new METHOD

- back to the `bank_acc_1_.py`

- Add a new method, name it `deposit()`

- SInce I am going to add the **balance + the amount** ,
  i will need to call() the `getBalance()` method from above within the `deposit()` method

<br>

```python
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()
```

<br>

### 🔶 Call it

- Go to the second file `bank_acc_1_.py` , and add the calling

```python
Sara.deposit(500)
# result
# As you can see, it added 500 to the 2000 (Sara s BALANCE)
#Account 'Sara' balance = $2500.00
```

<br>
<br>

### 🟢 Checking if we have enough balance to Complete the transaction

- Above the first class, add a second class

- name it: `BalanceException(Exception)`

```python
class BalanceException(Exception)
```

- now , below the `deposit()` **method.** add the **condition**

```python
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
```

<br>
<br>

#### 🟢 ADD a new METHOD

- In this new method I will Use the **Try** to <u>catch</u> **"error or exception"**

<br>

```python
     # 4 step
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

            #step 5 go to the bank_acc_1_.py
```

<br>

### In summary, these lines together represent a sequence of operations to perform a withdrawal from an account:

- Check if the withdrawal is allowed (viableTransaction method).

- Deduct the amount from the account balance.

- Print a message to confirm the withdrawal.

- Display the updated balance after the withdrawal.

<br>
<br>

### 🔶 Call it

- Go to the second file `bank_acc_1_.py` , and add the calling

- Purposely add an amount you don't have (like `10.000`) just to see what happens

```python
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
```

<br>
<br>

#### 🟢 ADD a new METHOD

- Performing a transfer between two accounts

```python
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

```

<br>

### 🔶 Call it

- Go to the second file `bank_acc_1_.py` , and add the calling

```python
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



```

#### In summary, these lines together represent a sequence of operations to perform a transfer between two accounts:
