# POLYPHORMISM

- Polymorphism in Python allows objects of different types to be treated as objects of a common base type.

> 🍊 This **means that you can create multiple classes that share a common interface or base class** and then use these classes interchangeably, depending on the context.

<br>
<br>

### 🎠 Explanation /PIZZA example

Imagine you're the master chef of a pizza parlor, and you've got a **magical 🤹‍♂️ oven** that can cook any type of pizza, whether it's loaded with pepperoni, veggies, or BBQ chicken.

- **polymorphism** is like having this **superpower** where you can treat all these different pizzas as if they're just regular pizzas.

<br>

let's dive into our pizza adventure!

- 🍕 Imagine we've got a bunch of pizzas with all sorts of yummy toppings. But here's the twist: each pizza has its own special recipe, like the Pepperoni Pizza, the Veggie Pizza, and the BBQ Chicken Pizza.

Now, imagine these pizzas as a big pizza family.

🟣 **The big boss pizza,** let's call it the "Pizza Boss", is the **superclass**. <u>It's like the head honcho pizza that all other pizzas look up to. </u>

🔶 Then, we've got the Pepperoni Pizza, the Veggie Pizza, and the BBQ Chicken Pizza as the little pizza siblings. They're all different but still part of the same pizza family.

<br>
<br>

#### So, polymorphism is like saying:

- "Hey, you know what? Even though you're a Pepperoni Pizza, a Veggie Pizza, or a BBQ Chicken Pizza, I can treat you **all** as if you're just regular pizzas!"

- Now, let's fire up that oven and get cooking! 🚀 **We'll loop through each** <u>pizza</u> in our pizza family, and even though they're all different, we'll use their special cooking methods. It's like having a pizza party where everyone brings their own flavor to the table!

#### That's polymorphism in action. Treating different pizzas as if they're all just part of the same delicious pizza family! 🍕🎉

<br>

```python
# The 👾 BIG BOSS pizza class that all the other pizzas look up to
#🌈
class PizzaBoss:
    def __init__(self, toppings):
        # constructor of the pizza BOSS
        self.toppings = toppings
        # REMEMBER: a constructor is a special method within a class that is automatically called when a new instance of the class is created. The constructor method is named __init__() and is used to initialize the object's attributes.


    # S SPECIAL method to represent the pizza when printed
    def __str__(self):
        return f"A pizza with {', '.join(self.toppings)} toppings 🌶️"
#----------
#
#
#
#


# 🟠 Pepperoni Pizza: A cool pizza with pepperoni toppings
class PepperoniPizza(PizzaBoss):

    def __init__(self, toppings):
        #
        #Calls the constructor of the pizza boss
        super().__init__(toppings)
        #In Python, **super()** is a build-in function used to access methods and properties from a parent class.

        #🍅METHOD cooking🥣
        # A special method only for veggie pizza
    def cook(self):
        return "Cooking Pepperoni Pizza"
#----------
#
#
#
#
# 🟠 Veggie Pizza: A groovy pizza loaded with veggies
class VeggiePizza(PizzaBoss):
    def __init__(self, toppings):
        # Calls the constructor of the pizza boss
        super().__init__(toppings)
        #
        #
        #

     #🍅METHOD cooking🥣
    # A special method only for Veggie Pizza
    def cook(self):
        return "Cooking veggie pizza"

#
#
#
#

#----------
# 🟠 BBQ Chickent Pizza: A sizzling pizza topped with BBQ chicken
class BBQChickenPizza(PizzaBoss):
    def __init__(self, toppings):
        # Calls the constructor of the pizza boss
        super().__init__(toppings)
        #
        #
        #
        #🍅METHOD cooking🥣
        # A special method only for BBQ Chicken Pizza
    def cook(self):
         return "Cooking BBQ chicken pizza"
#----------
#
#
#
## Our pizza party lineup with different types of pizzas

pizzas  = [
    PepperoniPizza(["cheese", "pepperoni 🐖"]),
    VeggiePizza(["cheese", "peppers🫑", "mushrooms 🍄"]),
    BBQChickenPizza(["cheese", "chicken 🐔", "BBQ sauce"])
]

#
#
#

# ------------------------------
## LOOP in the "pizzas options"
# ------------------------------
#
#
#

for pizza in pizzas:
    print("------")
    #  check what kind of pizza🟠 we are cooking
    print(pizza)

    # Now, lets use its 🍅 special METHOD cooking🥣
    print(pizza.cook())
    print("------")

## result

# ------
# A pizza with cheese, pepperoni 🐖 toppings 🌶️
# Cooking Pepperoni Pizza
# ------
# ------
# A pizza with cheese, peppers🫑, mushrooms 🍄 toppings 🌶️
# Cooking veggie pizza
# ------
# ------
# A pizza with cheese, chicken 🐔, BBQ sauce toppings 🌶️
# Cooking BBQ chicken pizza
# ------
```

### 2) example

#### BANKING system

- in this version below there is a part missing, i wanted to first concentrate on the structure of the parent and children

```python
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
# 🟣 Checking ACCOUNT:
# A basic account for day to day transactions
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
# 🟣 Savings Account:
# An account for saving money and earning interest
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
# 🟣 Investment Account:
#  An account for investing money in stocks and bonds
# --------------
class InvestmentAccount(BankAccountBoss):
    def __init__(self, account_number, balance):
        # Calls the constructor of the bank account
        super().__init__(account_number, balance)

    def invest(self, investment_amount):
        """
        Invest ...
        """
#
#
#
#
#---------------
# Our  banking   lineup with different types of accounts

accounts = [
    CheckingAccount("123456", 1000), # Checking Account
    SavingAccount("789012", 5000), #Savings Account
    InvestmentAccount("345678", 20000) # Investment Account
]
#---------------
#
#
#


#---------------
# Lets manage some money matters!
for account in accounts:
    #let's see what kind of account we're dealing with
    print(account)
    #
    #
    # Now, let's perform some banking weÄre dealing with
    if isinstance(account, CheckingAccount):
        print(account.fee_deduction(10)) # Deduct $10 as a transaction fee for checking account
    elif isinstance(account, SavingAccount):
        print(account.add_interest(3)) # Add 3% interest for savings account
    elif isinstance(account, InvestmentAccount):
        print(account.invest(5000)) # Invest $5000 in stocks for investment account
    print()

    # 🖐️ OUTPUT

#     Account Number: 123456, Balance: $1000
# None

# Account Number: 789012, Balance: $5000
# None

# Account Number: 345678, Balance: $20000
# None


```
