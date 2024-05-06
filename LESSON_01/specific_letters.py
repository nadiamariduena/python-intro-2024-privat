#--- reach specific letter from the vars below
first = 'Laure'
last = "Blaz"

# string index values
print(first[-1])
#result: e

first2 = 'Lorraino'
last2 = "Patsy"
#
#will remove the first and the last one
print(first2[1:-1])
# result: orrain
#
#
print(first2[1:])
# result: orraino

print("")

# -----
# Some methods return BOOLEAN
# - find if a word contains a specific letter, if yes then TRUE


print(first.startswith("D"))
# result: False
# --- check if the variable ends with Z
print(first2.endswith("Z"))

#
#
# BOOLEAN TPE

myvalue = True
x = bool(False)
# check the type
print(type(x))
print(isinstance(myvalue, bool))


#
#
# ------
# NUMERIC types

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
# it will check i its true its a number/integer
#result: <class 'int'>
#result: True

#
#
# ------
# Float types
# check if it a float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# Define a string "n" containing a numeric value

chiffre = "245.256"

# - convert the string "chifree" to floating-point number and print the result.

print(float(chiffre))