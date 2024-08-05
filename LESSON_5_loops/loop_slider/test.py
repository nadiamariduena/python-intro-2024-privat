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
