import pickle

# Example object representing a collection of shoes
class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

# Example collection of shoes
shoes_collection = [
    Shoe("Nike", 9, "Black"),
    Shoe("Adidas", 8, "White"),
    Shoe("Puma", 7, "Red")
]

# Serialize the shoes_collection object to a file
file_path = 'shoes_collection.pickle'
with open(file_path, 'wb') as file:
    pickle.dump(shoes_collection, file)

print(f"Serialized shoes collection to {file_path}")
