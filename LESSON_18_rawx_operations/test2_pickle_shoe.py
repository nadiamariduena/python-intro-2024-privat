#0
import pickle
#The pickle module is imported (import pickle).



# 1 Defining the Shoe Class:
#A Shoe class is defined with attributes brand, size, and color.
class Shoe:
#Instances of this class represent individual shoes with specific attributes.

    def __init__(self, brand, size, color):
        #It contains instances of the Shoe class initialized with different brands, sizes, and colors.

        self.brand = brand
        self.size = size
        self.color = color

# 2 Creating a List of Shoe Objects:
shoes_collection = [
    Shoe("Nike", 9, "Black"),
    Shoe("Adidas", 8, "White"),
    Shoe("Puma", 7, "Red")

]

#
#
# 3 Serialize the shoes collection object to a file
# - file_path Definition: Specifies the path where the serialized data will be stored, with a ".pickle extension".
# - .pickle extension indicating it will be a pickled file.
file_path = "this_will_be_the_generated_shoes_collection.pickle"
with open(file_path, "wb") as file:
    #open() Function: Opens the file specified by file_path in binary write mode ("wb").
    pickle.dump(shoes_collection, file)
    #dump() function: It takes two parameters - the object being “shoes_collection” (look at the shoes in line 11) and a File object (at the end of line 20) to write the data to.


#
# 4 Printing a Confirmation Message:
print(f"Serialized shoes collection to {file_path}")