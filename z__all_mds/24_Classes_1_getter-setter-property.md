## [Python Classes, Objects, Inheritance & Polymorphism for Beginners](https://youtu.be/RpBBzci_cBk?feature=shared)

<br>

# 🍭 GETTER & SETTERS

## What are Getters and Setters?

[source: datacamp.com ](https://www.datacamp.com/tutorial/property-getters-setters?utm_source=google&utm_medium=paid_search&utm_campaignid=21057859163&utm_adgroupid=157296744137&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=692112538027&utm_targetid=dsa-2218886984580&utm_loc_interest_ms=&utm_loc_physical_ms=9069516&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-es-lang-en_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&gad_source=1&gclid=Cj0KCQjwpZWzBhC0ARIsACvjWROhmuhx2Eg660jD0DS5PNlLRR-oya1jYobQWrwvzGS5as_CcgSKuMMaAtKJEALw_wcB)

**Getters:** These are the methods used in ✋ `Object-Oriented Programming (OOPS)` which helps to access the private attributes from a class.

**Setters:** These are the methods used in OOPS feature which helps to set the value to private attributes in a class.

<br>

### 🟠 Private Attribute - Encapsulation

- If you are not familiar with the private attributes or private methods in Python, read this [DataCamp article> role-underscore-python](https://www.datacamp.com/tutorial/role-underscore-python)

<br>
<br>

#### Getter Method:

A getter method, also known as an accessor method, is a method used to retrieve the value of a private attribute **( a variable that is not directly accessible from outside the class)**. It allows you to access the value of an attribute in a controlled manner.

#### Setter Method:

A setter method, also known as a mutator method, is a method used to modify the value of a private attribute. It provides a way to update the value of an attribute while enforcing certain conditions or validations.

#### 🔶 you need to declare the getter `@property` and setter ` @radius.setter` to use it

- you need to declare both **@property** and **@radius.setter** decorators if you want to use both the getter and setter methods within a single property in Python.

```python

# GETTER
    @property
    #
    #
    def radius(self):
        return self._radius

 # SETTER
    @radius.setter
    #
    #
    def radius(self, value):
        if value > 0:
            self._radius = value

```

#### @property decorator:

> This decorator is used to define a getter method for a property. When you decorate a method with @property, it becomes a property getter, and you can access it as if it were an attribute rather than a method.

#### @radius.setter decorator:

> This decorator is used to define a setter method for a property. When you decorate a method with @radius.setter, it becomes a property setter, and you can use it to set the value of the property as if it were an attribute assignment.

<br>
<br>

# Differences between Python `@Property` and `Getters & Setters`

- In Python, both @property and getters/setters are ways to control access to class attributes, but they do so in slightly different manners:

 <br>
 <br>

# `@Property`

#### 🔴 `@property` is used to get the value of a private attribute without using any getter methods. We have to put a line @property in front of the method where we return the private variable.

<br>

- **@property** is a Python <u>decorator</u> that **allows defining a method** that can be accessed like an attribute.

- 🟡 It's used to define a getter method for a class attribute.

- When the decorated method is called, it behaves like a read-only attribute, providing computed values or ensuring controlled access.

- It simplifies the syntax by allowing you to access the method like an attribute rather than a method call.

##### example:

```python
#  🟢  with PROPERT
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

# Creating an instance of Circle
my_circle = Circle(5)

# Accessing radius, diameter, and area like attributes
print("Radius:", my_circle.radius)
print("Diameter:", my_circle.diameter)
print("Area:", my_circle.area)


#
# ------------------
# 🟦 with GETTER & SETTER
# ------------------

class Circle:
    def __init__(self, radius):
        self._radius = radius


    # GETTER
    def get_radius(self):
        return self._radius
    # SETTER
    def set_radius(self, radius):
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = radius

    # GETTER
    def get_diameter(self):
        return 2 * self._radius
    # SETTER
    def get_area(self):
        return 3.14159 * self._radius ** 2

    # defining properties
    radius = property(get_radius, set_radius)
    diameter = property(get_diameter)
    area = property(get_area)

# Creating an instance of Circle
my_circle = Circle(5)

# Accessing radius, diameter, and area like attributes
print("Radius:", my_circle.radius)
print("Diameter:", my_circle.diameter)
print("Area:", my_circle.area)


```

#### me:

- so its cleaner to use `@properyty`, but confusing for beginners, as there is no way to know whcih is the `getter` and the `setter`

#### chatgpt:

**That's a valid point.** While `@property` simplifies syntax and enhances readability, especially for those familiar with Python, it might indeed be a bit confusing for beginners who are not aware of the getter and setter methods implicitly defined by the decorator.

Here's the same example with added comments for clarity:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    # getter
    def radius(self):
        """Getter method for the radius attribute."""
        return self._radius

    @radius.setter
    # @radius.setter is a decorator used in Python to define a setter method for a property.
    def radius(self, radius):
        """Setter method for the radius attribute."""
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = radius

    @property
    def diameter(self):
        """Getter method for the diameter attribute."""
        return 2 * self._radius

    @property
    def area(self):
        """Getter method for the area attribute."""
        return 3.14159 * self._radius ** 2

# Creating an instance of Circle
my_circle = Circle(5)

# Accessing radius, diameter, and area like attributes
print("Radius:", my_circle.radius)
print("Diameter:", my_circle.diameter)
print("Area:", my_circle.area)

```

### @radius.setter decorates the setter method immediately following it (def radius(self, radius)), indicating that this method should be associated with setting the radius property.

- So, when you try to assign a value to **my_circle.radius**, Python automatically calls the setter method **radius(self, radius)** with the assigned value, enabling you to perform any necessary validation or computations before setting the attribute `_radius`.

In simpler terms, it allows you to use `my_circle.radius =` value syntax to set the radius property, and the associated setter method radius(self, radius) will be invoked with the provided value.

<br>
<br>

# 🔴 In other words, similar to the useState `const [ state, setState] = useState()`?

#### chatgpt:

> Yes, in React's functional components, `useState()` **hook** is used to create state variables.

🟡 It returns an **array containing** the **current state** value as the **first element**, and a function to update the state as the **second element**.

The first element of the array serves as a getter to retrieve the current state value.

The second element of the array is a setter function used to update the state value.

##### Here's an example of how you would use useState():

```javascript
import React, { useState } from "react";

function Counter() {
  // Declare a state variable named 'count' with an initial value of 0
  const [count, setCount] = useState(0);

  // Event handler to increment the count
  const increment = () => {
    setCount(count + 1); // Updating the state using the setter function
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}

export default Counter;
```

<br>

```javascript
//  getter
🟢 `count` //serves as the state variable.
//
//
//  setter
🔵 `setCount` //is the setter function used to update the count state variable.
```

- `useState(0)` initializes the count state variable with an initial value of `0`.

- When the **"Increment"** button is clicked, the increment function is called, which uses <u>setCount</u> to update the <u>count</u> state variable by **incrementing its value**.

<br>
<br>

### 🟠 In javascript it would look like this:

In JavaScript, you can achieve similar functionality using object destructuring and function expressions.

- 🔴 While **JavaScript doesn't have** <u>built-in language</u> features like **Python's decorators** or React's hooks, you can create functions that act as **getters and setters** for object properties.

Here's an example of how you can create a simple Counter object with a private `_count` property and getter and setter methods for accessing and updating the count:

```javascript
const Counter = (() => {
  let _count = 0; // Private variable

  const getCount = () => _count; // Getter method
  // Setter method
  const setCount = (value) => {
    //
    if (typeof value === "number") {
      _count = value;
    } else {
      console.error("Invalid count value. Please provide a number.");
    }
  };

  return {
    getCount,
    setCount,
  };
})();

// Get the initial count
console.log("Initial count:", Counter.getCount());

// Set a new count
Counter.setCount(5);

// Get the updated count
console.log("Updated count:", Counter.getCount());
```

We use an **immediately-invoked function expression (IIFE)** to create a closure for the Counter object, providing private scope for the \_count variable.

Inside the closure, we define getter and setter methods (getCount and setCount) for accessing and updating the count.

🟡 The Counter object returned from the **IIFE** contains the getter and setter methods, allowing external code to interact with the count property indirectly.

We demonstrate getting the initial count, **setting a new count**, and **getting the updated count** using the getter and setter methods.

#### While this approach in JavaScript is more verbose compared to Python's decorators or React's hooks,

it achieves similar functionality by encapsulating private state and providing controlled access to it through getter and setter methods.
