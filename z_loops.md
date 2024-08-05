# 🟡 LOOPS

<br>

## 🟦 For loops

### Slider Basic


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

