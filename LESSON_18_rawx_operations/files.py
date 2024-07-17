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
# print(f.read())
#print(f.read(4)) # it will reach the first 4 character file, which in this case will be Dave

for line in f:
    print(line)

print("----")

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exists")
finally:
    f.close()


#
print("_____ 👾 ______")
# ------
#
# APPEND 1. ('a') a: stands for APPEND
# ------
f = open('names.txt', 'a')
f.write('David Lee Roth 🥥')
f.close()

f = open('names.txt')
print(f.read())
f.close()
#
#
#
print("_____ 🦄 ______")
#
#
# ------
# WRITE ('w') w: stands for WRITE
# write & Overwrite, we will overwrite what we have, when we will open the txt
# ------

f = open("context.txt", "w")
