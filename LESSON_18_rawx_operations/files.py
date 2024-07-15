# Acronym for:

# r = Read
# a = Append
# w = Write
# x = Create

# Read - Error if the file doesn't exist
# f stands for FILE
# r stands for read, i will use it here below,  as the second argument

# f = open("names.txt", "r") # the r is telling it to read the file, but without the r, it also tells it to read the file, but only when its the r alone

f = open("names.txt")
print(f.read())