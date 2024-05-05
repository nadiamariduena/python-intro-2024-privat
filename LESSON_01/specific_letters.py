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