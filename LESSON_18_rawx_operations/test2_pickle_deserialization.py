
# 1 once you have generated the pickle by using the code:
# 2 test2_pickle_shoe.py
# use the below code to convert the binary file that was generated on step 2 code




import pickle

# Define the Shoe class
class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color

# File path where the pickled data is stored
file_path = "this_will_be_the_generated_shoes_collection.pickle"

# Deserialize (unpickle) the objects from the pickle file
with open(file_path, "rb") as fdile:
    loaded_shoes_collection = pickle.load(fdile)

# Now you can work with the loaded objects
print("Deserialized shoes collection:")
for shoe in loaded_shoes_collection:
    print(f"Brand: {shoe.brand}, Size: {shoe.size}, Color: {shoe.color}")

