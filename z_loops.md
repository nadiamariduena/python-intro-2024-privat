# 🟡 LOOPS

<br>



### Before starting with the for loop, check the version below:

```python
# Starting Value of the slider

slider_value = 50 # Ltes say the slider start at the middle ( think about a sequence of 3 imgs, 0,1,2 , it will start from picture 1)



# ---------
def increase_slider(amount):
    global slider_value

    slider_value += amount
    # add amount to the slider_value

    if slider_value > 100: #means (if the slider has reached the end) , then do the below:
        slider_value = 100 # Cap the slider at 100 (This will ensure that the slider value does not go beyond its maximum limit)

    print(f"Slider increased to: {slider_value}")

# ---------
# Function to decrease the slider value
def decrease_slider(amount):
    global slider_value

    slider_value -= amount

    if slider_value < 0:
        slider_value = 0 # Floorthe slider at o (remember:  0,1,2 )

    print(f"Slider decreased to: {slider_value}")

# ---------

#

# Simulate some changes (i will explain the below in the nex example)
increase_slider(10)  # Increase the slider by 10
decrease_slider(20)  # Decrease the slider by 20
increase_slider(50)  # Increase the slider by 50
decrease_slider(60)  # Decrease the slider by 60
```

<br>

**increase_slider(amount)**:


 This function **adds** a certain **amount** to the **slider’s current value** using the **+= operator**.


- -  If the slider value exceeds 100, it sets the value to 100 (since the slider can't go beyond 100).

<br>

**decrease_slider(amount)**: This function **subtracts** a certain **amount** from the  **slider’s current value** using the **-= operator**.

- - If the slider value goes below 0, it sets the value to 0 (since the slider can't go below 0).

<br>

### 🟢 Global

- Global is  a keyword **used** to **declare** that a **variable inside** a function **refers** to **a variable defined outside** the function.


- - It allows you to modify the global variable from within a function.

### 🟧 Purpose of global

**Scope of Variables:** Variables defined inside a function are local to that function. They can’t be accessed or modified outside of it.

<br>

**Modifying Global Variables:** When you want to modify a global variable (a variable defined outside of any function) from within a function, you need to use the global keyword.

- -  This tells Python that you are referring to the global variable, not creating a new local one.

```python
# Global variable
count = 0

def increment():
    global count  # Declare that we are using the global variable 'count'
    count += 1    # Modify the global variable 'count'

def display():
    print(count)  # Access the global variable 'count'

increment()  # Calls the increment function
display()    # Prints the updated value of 'count'

```

<br>
<br>
<br>


## 🟦 For loops

### Slider Basic
<br>




## 🌈 Reset the slider after reaching the limit

The GOAL is to make the slider to **wrap** around and **return to 0 (or another value like 10)** <u>once it reaches its maximum value (100)</u> , you can modify the previous code to include this behavior.


####  🟧 Here’s how you can adjust the functions to make the slider reset to 0 after reaching 100 and to 10 after reaching 100 in a more interactive loop:




<br>
<br>

```python
slider_value = 50


# Define wrap-around limits

MIN_VALUE = 0
MAX_VALUE = 100
WRAP_VALUE = 10 # Will reset the value when the slider exceeds MAX_value

# Function to increase the slider value

def increase_slider(amount):

    global slider_value

    slider_value += amount

    if slider_value > MAX_VALUE:
        slider_value = WRAP_VALUE # RESET to wrap around value

    print(f"Slider INCREASED to: {slider_value}")

def decrease_slider(amount):

    global slider_value

    if slider_value < MIN_VALUE:

        slider_value = MAX_VALUE

    print(f"Slider DECREASED to: {slider_value}")


# Simulate changes in a loop

adjustments = [
    ('increase', 10),
    ('decrease', 20),
    ('increase', 50),
    ('decrease', 60),
    ('increase', 80),  # This should wrap around to 10
]


for action, amount in adjustments:
    if action == "increase":
        increase_slider(amount)
    elif action == "decrease":
        decrease_slider(amount)
```

<br>
<br>


#### 🟣 Question:  what is the purpose of having 2 (one a the bottom and one at the top?


```python
# Define wrap-around limits
MIN_VALUE = 0
MAX_VALUE = 100
WRAP_VALUE = 10  #

compared to the one at the bottom

adjustments = [
    ('increase', 10),
    ('decrease', 20),
    ('increase', 50),
    ('decrease', 60),
    ('increase', 80),  # This should wrap around to 10
]
```

<br>

### ✅ chatgpt:

**Great** question! Both sets of variables serve different purposes in the code, and understanding their roles can clarify how the slider works.
