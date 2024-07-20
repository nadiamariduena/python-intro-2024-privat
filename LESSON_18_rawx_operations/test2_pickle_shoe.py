import pickle


class Shoe:

    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

shoes_collection = [
    Shoe("Nike", 9, "Black"),
    Shoe("Adidas", 8, "White"),
    Shoe("Puma", 7, "Red")

]

# Serialize the shoes collection object to a file
file_path = "this_will_be_the_generated_shoes_collection.pickle"
with open(file_path, "wb") as file:
    pickle.dump(shoes_collection, file)