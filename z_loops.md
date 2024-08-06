# 🟡 LOOPS

- images used in the slider:  [Tima Miroshnichenko](TimaMiroshnichenko)

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


<br>
<br>


### 🟠  Wrap-Around Limits



```python
# Define wrap-around limits
MIN_VALUE = 0
MAX_VALUE = 100
WRAP_VALUE = 10  # The value to reset to when the slider exceeds MAX_VALUE

```

<br>

**MIN_VALUE:**

- -  Represents the minimum value the slider can have. In this case, it's set to 0.


**MAX_VALUE:**

- - Represents the maximum value the slider can have. In this case, it's set to 100.

<br>

**WRAP_VALUE:**

- -  Specifies the value to which the slider should reset when it exceeds MAX_VALUE. Here, it's set to 10, meaning that if the slider value goes over 100, it will wrap around to 10.


<br>

### 🟠 Adjustments List


```python
adjustments = [
    ('increase', 10),
    ('decrease', 20),
    ('increase', 50),
    ('decrease', 60),
    ('increase', 80),  # This should wrap around to 10
]
```

<br>

- **adjustments List:** This list contains **tuples `[()]`** that specify actions and amounts to be performed on the slider. Each tuple has an action ('increase' or 'decrease') and a corresponding amount.


<br>
<br>

### 🟣 question: in other words the top settings is just to have a control over the reset, and the one at the bottom is for the user to give it control to go forward or backwards if implemented with buttons?

#### ✅ chatgpt:

- - Exactly! You've got it right.








<br>

<br>

### 🟣 QUESTION:  so this `('increase', 10), ('decrease', 20), etc` properties are connected to the `if action == "increase":` of the loop ?

#### ✅ chatgpt:

- - Yes, exactly! The ('increase', 10) and similar tuples in the adjustments list are directly connected to the if action == "increase": part of the loop. Here’s how they work together:


<br>

### How It All Connects

**Adjustments List:**

This list contains **tuples** like `('increase', 10)` which specify what action to take and by how much.

```python
# wrong
adjustments = [
    ('increase__', 10),
    ('___decrease', 20),
    ('increase______', 50),
    ('_________decrease', 60),
    ('increase________________', 80),  # This should wrap around to 10
]


# GOOD 👍

adjustments = [
    ('increase', 10),
    ('decrease', 20),
    ('increase', 50),
    ('decrease', 60),
    ('increase', 80),  # This should wrap around to 10
]


```

<br>

**Each tuple** represents an instruction to either **increase or decrease** the slider’s value.

```python

if action == 'increase':
    increase_slider(amount)
elif action == 'decrease':
    decrease_slider(amount)

```

<br>

### Loop:

The for loop iterates through each tuple in the adjustments list.
For each tuple, the loop checks the action part of the tuple to decide what to do.



<br>
<br>


## 🟦 for file in image_files:

<br>

### 🟠 Show images with Tkinter

#### 🔴 At the moment, I’m not actively focusing on Tkinter. However, I’m including the code below to familiarize myself with it. In the future, as I become more comfortable with Python, I may find ways to incorporate Tkinter into my projects.


- 🟤 create a folder where you will store the code below and the images,  within it create you `.venv` then activate it

<br>

```python
# install this
from PIL import Image, ImageTk # pip install pillow


import requests # pip install requests
# if you dont install this, you will have an error
```

<br>

- There are many aspects here that I still need to understand, but I wanted to check if the images would display correctly.



```python

import tkinter as tk
from PIL import Image, ImageTk

import requests
from io import BytesIO

# Initialize the main window
root = tk.Tk()
root.title("Image Slider")

# URLs of the images
image_urls = [

    "https://images.pexels.com/photos/25413123/pexels-photo-25413123/free-photo-of-campagne-cloture-barriere-grillage.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/25413122/pexels-photo-25413122/free-photo-of-route-aube-cote-littoral.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load",
    "https://images.pexels.com/photos/18486577/pexels-photo-18486577/free-photo-of-bois-paysage-art-sale.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/18264586/pexels-photo-18264586/free-photo-of-mer-paysage-ciel-soleil-couchant.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",

]

# Function to download images and convert to PhotoImage
def load_images_from_urls(urls):
    images = []
    for url in urls:
        response = requests.get(url)
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img = img.resize((300, 200), Image.ANTIALIAS)  # Resize image if needed
        photo = ImageTk.PhotoImage(img)
        images.append(photo)
    return images

# Load images
images = load_images_from_urls(image_urls)

# Create a canvas to display the images
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Function to update the image on the canvas
def update_image(value):
    if 0 <= value <= 100:
        index = value // 10  # Determine which image to show
        canvas.delete("all")  # Clear the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=images[index])
    else:
        print("Value out of range")

# Initialize the slider
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_image)
slider.pack()

# Initialize the slider value to display the first image
update_image(slider.get())

# Run the Tkinter event loop
root.mainloop()

```

- I am bit tired, i think i found the reason and its stupid because obviously its related to the variables connected to the images and also the enumeration (i will try to find more issues tomorrow)

```python
# 🔴 remember the css slider and the framer animation on fade (when all images appeared in 2seconds and disappeared to only leave 1 ) when you dont use ID, the number on the image is the id

    PhotoImage(file="image0.png"),  # Image for value 0
    PhotoImage(file="image10.png"), # Image for value 10
    PhotoImage(file="image20.png"), # Image for value 20
    PhotoImage(file="image30.png"), # Image for value 30
    PhotoImage(file="image40.png"), # Image for value 40
    PhotoImage(file="image50.png"), # Image for value 50
    PhotoImage(file="image60.png"), # Image for value 60
    PhotoImage(file="image70.png"), # Image for value 70
    PhotoImage(file="image80.png"), # Image for value 80
    PhotoImage(file="image90.png"), # Image for value 90
    PhotoImage(file="image100.png") # Image for value 100
```

 <br>

### 🔴 Works but too small

```python
import tkinter as tk
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("Image Slider")

# Function to load images
def load_image(filename):
    image = Image.open(filename)
    return ImageTk.PhotoImage(image)

# List of image filenames
image_files = [
    "image0.png",
    "image10.png",
    "image20.png",
    "image30.png",
    "image40.png",
    "image50.png",
    "image60.png",
    "image70.png",
    "image80.png",
    "image90.png",
    "image100.png"
]

# Load images into a list
images = []
for file in image_files:
    try:
        img = load_image(file)
        images.append(img)
    except Exception as e:
        print(f"Error loading image {file}: {e}")

# Create a canvas to display the images
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Function to update the image on the canvas
def update_image(value):
    try:
        value = int(value)
        if 0 <= value <= 100:
            index = value // 10  # Determine which image to show
            canvas.delete("all")  # Clear the canvas
            canvas.create_image(0, 0, anchor=tk.NW, image=images[index])
            canvas.image = images[index]  # Keep a reference to avoid garbage collection
        else:
            print("Value out of range")
    except Exception as e:
        print(f"Error updating image: {e}")

# Initialize the slider
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_image)
slider.pack()

# Initialize the slider value to display the first image
update_image(slider.get())

# Run the Tkinter event loop
root.mainloop()

```

<br>
<br>

### 🔴 Works but stretch the image

```python
import tkinter as tk
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("Image Slider")

# Function to load and resize images
def load_and_resize_image(filename, size=(600, 600)):
    image = Image.open(filename)
    image = image.resize(size, Image.ANTIALIAS)  # Resize image
    return ImageTk.PhotoImage(image)

# List of image filenames
image_files = [
    "image0.png",
    "image10.png",
    "image20.png",
    "image30.png",
    "image40.png",
    "image50.png",
    "image60.png",
    "image70.png",
    "image80.png",
    "image90.png",
    "image100.png"
]

# Load and resize images
images = []
for file in image_files:
    try:
        img = load_and_resize_image(file)
        images.append(img)
    except Exception as e:
        print(f"Error loading image {file}: {e}")

# Create a canvas to display the images with a size of 600x600
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Function to update the image on the canvas
def update_image(value):
    try:
        value = int(value)
        if 0 <= value <= 100:
            index = value // 10  # Determine which image to show
            canvas.delete("all")  # Clear the canvas
            canvas.create_image(0, 0, anchor=tk.NW, image=images[index])
            canvas.image = images[index]  # Keep a reference to avoid garbage collection
        else:
            print("Value out of range")
    except Exception as e:
        print(f"Error updating image: {e}")

# Initialize the slider
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_image)
slider.pack()

# Initialize the slider value to display the first image
update_image(slider.get())

# Run the Tkinter event loop
root.mainloop()

```

<br>
<br>


### 🔴 Works but not centered

```python
import tkinter as tk
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("Image Slider")

# Function to load and resize images while maintaining aspect ratio
def load_and_resize_image(filename, max_size=(600, 600)):
    #
    #
    image = Image.open(filename)
    #
    # Resize the image to fit within the specified max_size while preserving the aspect ratio
    image.thumbnail(max_size, Image.ANTIALIAS)  # Resize image while maintaining aspect ratio

    #
    # Convert the PIL image to a format Tkinter can use

    return ImageTk.PhotoImage(image)

# List of image filenames
image_files = [
    "image0.png",
    "image10.png",
    "image20.png",
    "image30.png",
    "image40.png",
    "image50.png",
    "image60.png",
    "image70.png",
    "image80.png",
    "image90.png",
    "image100.png"
]

# Load and resize images into a list
images = []
for file in image_files:
    #

    try:
        # Load and resize each image, then add it to the 'images' list
        img = load_and_resize_image(file)
        images.append(img)
        #
        #
    except Exception as e:
    # Print an error message if the image cannot be loaded
        print(f"Error loading image {file}: {e}")

# Create a canvas with a fixed size
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

# Function to update the image on the canvas
def update_image(value):
    try:
        value = int(value)

        # Ensure the slider value is within the expected range
        if 0 <= value <= 100:

            # Determine the index of the image to display based on slider value
            index = value // 10  # Determine which image to show
            image = images[index]
            image_width, image_height = image.width(), image.height()

            # Calculate the scaling factor to fit the image within the canvas
            canvas_width = canvas.winfo_width()
            # canvas_width = canvas.winfo_width(): Gets the current width of the canvas.
            # canvas_height = canvas.winfo_height(): Gets the current height of the canvas.
            canvas_height = canvas.winfo_height()

            # Calculates the scaling factor.
            # - This factor ensures that the image fits within the canvas without exceeding its dimensions.
            # - The min function ensures the image is scaled down by the smallest factor, so it fits both width and height.
            scale = min(canvas_width / image_width, canvas_height / image_height)

            # Resize image based on the scaling factor
            new_width = int(image_width * scale) # Computes the new width of the image after scaling.

            new_height = int(image_height * scale)
            # Computes the new height of the image after scaling.
            #
            resized_image = image._PhotoImage__photo.zoom(new_width // image_width, new_height // image_height) # Resizes the image based on the calculated dimensions. The zoom method scales the image by the ratio of the new size to the original size.

            # Clear the canvas and display the resized image
            canvas.delete("all")
            canvas.create_image(0, 0, anchor=tk.NW, image=resized_image)
            canvas.image = resized_image  # Keep a reference to avoid garbage collection
        else:
            print("Value out of range")
    except Exception as e:
        print(f"Error updating image: {e}")


# 🤚 SLIDER
# Initialize the slider
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_image)
# Creates a slider that ranges from 0 to 100. The update_image function is called whenever the slider value changes.
slider.pack(fill=tk.X) # Makes the slider fill horizontally.

# Run the Tkinter event loop
root.mainloop()
```