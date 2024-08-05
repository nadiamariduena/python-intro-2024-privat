# Starting Value of the slider

slider_value = 50 # Ltes say the slider start at the middle ( think about a sequence of 3 imgs, 0,1,2 , it will start from picture 1)

def increase_slider(amount):
    global slider_value

    slider_value += amount
    # add amount to the slider_value

    if slider_value > 100: #means (if the slider has reached the end) , then do the below:
        slider_value = 100 # Cap the slider at 100 (This will ensure that the slider value does not go beyond its maximum limit)

    print(f"Slider increased to: {slider_value}")