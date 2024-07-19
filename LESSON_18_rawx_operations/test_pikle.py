import pickle

example_dict = {1:"6", 2:"2",3:"f"}


pickle_out = open("dict.pickle", "wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

# - 1 Run the code, it will generate a binary file called "dict.pickle"
# - 2 you will not be able to visualize it, but you can install the below extension:
# - 3 Within your extensions, Install: Hex Editor Extension
# - 4 Once installed, click on the generated "dict.pickle" , click on the blue button, it will offer you to options at the top bar, choose the option of Hex editor

# OUTPUT
