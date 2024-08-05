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

# Load and resize images
images = []
for file in image_files:
    try:
        img = load_and_resize_image(file)
        images.append(img)
    except Exception as e:
        print(f"Error loading image {file}: {e}")

# Create a canvas with a fixed size
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

# Function to update the image on the canvas
def update_image(value):
    try:
        value = int(value)
        if 0 <= value <= 100:
            index = value // 10  # Determine which image to show
            image = images[index]
            image_width, image_height = image.width(), image.height()

            # Calculate the scaling factor to fit the image within the canvas
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()
            scale = min(canvas_width / image_width, canvas_height / image_height)

            # Resize image based on the scaling factor
            new_width = int(image_width * scale)
            new_height = int(image_height * scale)
            resized_image = image._PhotoImage__photo.zoom(new_width // image_width, new_height // image_height)

            # Clear the canvas and display the resized image
            canvas.delete("all")
            canvas.create_image(0, 0, anchor=tk.NW, image=resized_image)
            canvas.image = resized_image  # Keep a reference to avoid garbage collection
        else:
            print("Value out of range")
    except Exception as e:
        print(f"Error updating image: {e}")

# Initialize the slider
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_image)
slider.pack(fill=tk.X)

# Run the Tkinter event loop
root.mainloop()
