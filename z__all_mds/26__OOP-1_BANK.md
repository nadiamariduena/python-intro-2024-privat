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

#### Now within the second file `bank_acc_1_.py`

- I will add the below code to show the account name and balancem based on the above code

```python
# the *: stands for import ALL
from bank_accounts_0 import *

Dave = bank_account(1000, "Dave")
Sara = bank_account(2000, "Sara")
```

#### result

```
Account 'Dave' created.
Balance = $1000.00

Account 'Sara' created.
Balance = $2000.00
```
