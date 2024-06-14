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
