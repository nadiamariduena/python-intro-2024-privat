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

- Print a message indicating the start of the transfer.

- Check if the transfer is feasible (viableTransaction method).

- Withdraw funds from the sender's account.

- Deposit funds into the recipient's account.

- Print a message confirming the successful completion of the transfer.

<br>
<br>

### 🟣 NEW class / interest Reward

- this class will be responsible for adding **5% increase** to the account

- this class has the inherited data from the parent class `class bank_account`

```python
 # 🟠 1 step
 #parent class
class bank_account:
```

<br>

### Below you will be passing the default data and you will add to this 2 arguments a 5 percent increase

```python

class bank_account:
    def __init__(self, initialAmount, accountName):
```

#### at the end you will have the following output

```python
# 1 DEFAULT: b default Jim has 1000
# Account 'Jim' balance = $1000.00
# Deposit COMPLETE 🎁

# ---------
#✋ 2 the reward with the 5%
# Account 'Jim' balance = $1105.00
```

<br>
<br>

```python
    # inherited data from the above class
    #
    # child of the  "bank_account" in step 1
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
```

### 🔶 Call it

- Go to the second file `bank_acc_1_.py` , and add the calling

```python

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

# ---------
#✋ the reward with the 5%
# Account 'Jim' balance = $1105.00
#
# Transfer
Jim.transfer(100, Dave)
```

<br>
<br>

### 🟣 NEW class / SavingsAccount

- this class will be responsible for adding **5 dollar FEE** to the account

```python

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
```

<br>

---

<br>

## 🟨 Recapitulatif:

### 🔸 Question: what is the difference between this 2 classes, they are both part of the parent class `bankingaccount` in step 1, but their structure is different, why do i need the `__init__ and super` on the 2 class?

```python
1
class InterestRewardsAccount(bank_account):
def deposit(self, amount):
self.balance = self.balance + (amount * 1.05)

2
class SavingsAccount(InterestRewardsAccount):
def init(self, initialAmount, accountName):
super().init(initialAmount, accountName)
```

#### chatgpt:

- This class **InterestRewardsAccount** , extends (inherits from) a class named `bank_account`.

- It defines a method `deposit(self, amount)` that **increases the balance** by **5%** of the deposited amount (amount \* 1.05).

```python
class InterestRewardsAccount(bank_account):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)

```

#### chatgpt:

- This class **SavingsAccount** extends (inherits from) `InterestRewardsAccount`.

- It has an `__init__` method that takes two parameters (**initialAmount** and **accountName**).

- Inside `__init__`, it calls `super().__init__(initialAmount, accountName)`, which <u>✋invokes </u> the **init** method of the **superclass** `(InterestRewardsAccount)`.

<br>

### 🔸 QUESTION: In other words..the first class in the above code `class InterestRewardsAccount`, gets the data from the the parent class `bank_account` and the 2 class `class SavingsAccount` gets the data from the InterestRewardsAccount but since initialAmount and accountName are methods from the parent class, i need to `__init__` it and then use the `super` to clarify or invoke i really want to use them?

### ✅ Yes, you're correct in understanding the relationship between the two classes and the use of **init** and super().

<br>
<br>

> In object-oriented programming, when you have a **subclass** (like SavingsAccount) that inherits from a superclass (InterestRewardsAccount), here's how it works regarding initialization and attributes:

**Inheritance:**

✋ `SavingsAccount` **inherits all methods and attributes** from `InterestRewardsAccount`. This means SavingsAccount can use all methods defined in InterestRewardsAccount, including the deposit method that adds 5% interest.

Inside SavingsAccount's `__init__` method, you call `super().__init__(initialAmount, accountName)`. This line does two things:

- It calls the **init** method of the superclass (InterestRewardsAccount). This ensures that any initialization logic defined in InterestRewardsAccount is executed when creating an instance of SavingsAccount.

- It passes initialAmount and accountName to the superclass's **init** method, allowing InterestRewardsAccount to initialize its own attributes if necessary.

<br>

### Why use super():

By using `super().__init__(initialAmount, accountName)`, you explicitly invoke the initialization of the superclass (InterestRewardsAccount).

This is important because the superclass might have its own attributes or initialization logic that should be executed when creating instances of both InterestRewardsAccount and its subclasses like SavingsAccount.

> ✋ It clarifies that when you create a **SavingsAccount**, you want the initialization process to also include the initialization steps defined in **InterestRewardsAccount**, ensuring a complete and consistent initialization procedure.

<br>

#### 🌈 In summary, `__init__ and super()` are used in the `SavingsAccount` class to ensure that:

- **The subclass** (`SavingsAccount`) can define its own initialization logic and attributes (initialAmount and accountName).

- **The superclass's** (`InterestRewardsAccount`) initialization logic is also executed, maintaining the integrity of the object's state and behavior as defined by both classes in the inheritance hierarchy.
  <br>

### 🔸 QUESTION: In other words, if I add only one of the arguments of the parent class within the super(), would I have some sort of behavior? I thought that, like in React, I could destructure and retrieve exactly what I need from an argument.

### ✅ Yes, that's correct. When you use super() to call a method from the parent class (superclass), you need to pass all the required arguments that the parent class's method expects. ✋ If you omit any required arguments, Python will raise an 🔴error indicating that the method was called with missing arguments.

> 🔴 In Python, when you use super() to call a method from the parent class (superclass), you must provide all the arguments that the parent class's method expects. **Unlike destructuring** in languages like JavaScript, where you can selectively pick properties from an object.

#### ✋Python requires you to pass the exact number of arguments expected by the method being called via super(). 🔴

<br>

- **ERROR** with the below code ou will get an error

```python
class ParentClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

class ChildClass(ParentClass):
    def __init__(self, arg1):
        super().__init__(arg1)  # ❌ Incorrect usage
# ISSUE
# When ChildClass calls super().__init__(arg1), it only provides one argument (arg1). However, ParentClass expects two arguments (arg1 and arg2).
#
#
# Python will raise a TypeError because you didn't provide all the arguments required by ParentClass's __init__ method.
```

#### Solution:

To correctly call the parent class's **init** method from the child class, you need to pass both arg1 and arg2, even if ChildClass doesn't directly use arg2. This is how you should correct

```python
class ChildClass(ParentClass):
    def __init__(self, arg1):
        super().__init__(arg1, None)  # Pass None or some default value for arg2 if not used

```

<br>
<br>

### Lets continue

Each line in this method serves a specific purpose related to **handling a withdrawal transaction** from an account, **including:** validation, balance adjustment, status reporting, and error handling.

```python

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
               print("\nWithdraw completed.") # Prints a message confirming that the withdrawal process has been successfully completed.


               self.getBalance()
               #
               # Calls getBalance() to retrieve and display the updated balance after the withdrawal.

               # if a BalanceException is raised during the withdrawal attempt (e.g., insufficient funds), the program jumps to this line to handle the exception.
           except BalanceException as error:
               print(f"\nWithdraw interrupted: {error}")

```
