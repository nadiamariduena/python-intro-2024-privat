
#----------
# LOOP
#----------
#
#
# list of "people" with their name, age, and height
# 1)
people = [
    # the 165.5 will be rounded
    {"name": "Alice", "age": 30, "height": 165.5},
    {"name": "Bob", "age": 25, "height": 180.0},
    {"name": "Charlie", "age": 35, "height": 175.2}
]

#
# 2) LOOP
# Loop through each person in the list
for person in people:
    # extract variables from the dictionary
    name = person["name"]
    age = person["age"]
    height = person["height"]



#
# 3) Format the string using f-string with formatting options
#
message_e = f"Name: {name}, Age:{age}, Height: {height:.2f} cm"
#🔴 In the context of the format specifier {:.2f}, the f indicates that the variable should be formatted as a floating-point number.

print(message_e)