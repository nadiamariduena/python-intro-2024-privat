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
    ('increase__', 10),
    ('___decrease', 20),
    ('increase______', 50),
    ('_________decrease', 60),
    ('increase________________', 80),  # This should wrap around to 10
]


for action, amount in adjustments:
    if action == "increase":
        increase_slider(amount)
    elif action == "decrease":
        decrease_slider(amount)