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

```python
class bank_account:
    def __init__(self, initialAmount, accountName):

        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        # remember: the :.2 will format the balance outcome to a 2 decimal points, so it will represent the cents
```

<br>

> `${self.balance:.2f}` formats the **self.balance** attribute as a floating-point number with two decimal places. This is a common way to represent currency or precise numerical values in Python.

<br>
