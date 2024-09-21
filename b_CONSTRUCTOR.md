# 🟡 CONSTRUCTOR

<br>

### 🧸 playful explanation ⤵️  [Go to section](#constructor_playful_)



<br>
<br>
<br>

<br>
<br>

## 🫐 🟡 CONSTRUCTOR

<a name="constructor_serious_"></a>

- **a constructor** is a special method within a class that is automatically called when a new instance of the class is created. The constructor method is named `__init__()` and is used to initialize the object's attributes.

#### 🟡 `__init__`

<br>

Here's a breakdown of its purpose and usage:

**Initialization:** The primary purpose of a constructor is to initialize the newly created object with any necessary initial values. This typically involves setting the initial state of instance variables (also known as attributes) within the object.

**Automatic Invocation:** When you create a new instance of a class using the class name followed by parentheses (e.g., `obj = MyClass())`, Python automatically invokes the constructor method `__init__().`

**Customization:** You can define the constructor to accept parameters, allowing you to customize the initialization process based on specific values passed during object creation. These parameters are passed as arguments to the `__init__()` method.

<br>

### Here's a basic example to illustrate the concept:

<br>

```python
class Person:

   def __init__(self, name, age):
      self.name = name
      self.age = age

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes of the object

print(person1.name) # output: Alice
print(person1.age) # output: 30

```
