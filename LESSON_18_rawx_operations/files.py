# Acronym for:

# r = Read
# a = Append
# w = Write
# x = Create

# Read - Error if the file doesn't exist
# f stands for FILE
# r stands for read, i will use it here below,  as the second argument

# f = open("names.txt", "r") # The 'r' indicates that it is reading the file. Without the 'r', it also reads the file, but only when 'r' is the sole parameter.

f = open("names.txt")
print(f.read())