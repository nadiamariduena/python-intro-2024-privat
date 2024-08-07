# FOR loop
#
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
