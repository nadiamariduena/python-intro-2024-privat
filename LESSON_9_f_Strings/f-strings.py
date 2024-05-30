person = "Dave"
coins = 3


# OLder way of doing it
print("\n" + person + " has " + str(coins) + " coins left." )

# this is also an OLDER way of doing it
# Lets find another way of creating the same string
message = "\n%s hass %s coins left." % (person, coins)
print(message)
# RESULT
# Dave hass 3 coins left.
#
#
# Modern way of doing it
messageTwo = "\n{} has {} coinss left.".format(person, coins)
print(messageTwo)
# Dave has 3 coinss left.
#
# -------- another example
messageThree = "\n{1} has {0} coinss left.".format(person, coins)
print(messageThree)
# 3 has Dave coinss left.
messageFourth = "\n{1} has {0} coinss left.".format(coins, person)
print(messageFourth)
# result
#Dave has 3 coinss left.
#-----------
# another example
messageFifth = "\n{person} has {coins} coinss left.".format(coins=coins, person=person)
print(messageFifth)
# result
#Dave has 3 coinss left.
#
#
# example with dictionary
#
# check that person has colons
playerr = {'personn': 'Dave', 'coinss': 8}


message_a = "\n{personn} has {coinss} coins left.".format(**playerr)
print(message_a)
# result
#Dave has 8 coins left.
#
#
# F-STRINGS
user = "Nataly"
amount = "5"

message_b = f"\n{user} has {amount} coins left."
print(message_b)
# result
# Nataly has 5 coins left.

#
#
message_c = f"\n{user} has {2 + 7} coins left."
print(message_c)
# result
#Nataly has 9 coins left.
#
#
# with methods
# with the lower() method, the user Nathaly, should be lower
message_d = f"\n{user.lower()} has {2 + 7} coins left."
print(message_d)
# result
# nataly has 9 coins left.
#
#
#-------------
# Example with dictionary 2)
# check that person2 has colons: as the person2 is the key
player2 = {'person2': 'Nuria', 'savings': 500}
#

message_e = f"\n{player2['person2']} has {2 + 5} coins left."
print(message_e)

#
#----------------
# PASSING OPTIONS
# you can pass formatting options

# Define variables
name = "Alice"
age = 30
height = 165.5

# Format the string using f-string with formatting options
message = f"Name: {name}, Age: {age}, Height: {height:.2f} cm"
# 🔴 {height:.2f} is replaced by the value of the height variable formatted as a floating-point number with two decimal places.

# Print the formatted message
print(message)

#
#
#----------
# LOOP
#----------
#
#
# list of "people" with their name, age, and height
#
people = [
    # the 165.5 will be rounded
    {"name": "Alice", "age": "30", "height": "165.5"},
    {"name": "Bob", "age": "75", "height": "180.0"},
    {"name": "Auri", "age": "25", "height": "175.2"},
]

#
# LOOP
# Loop through each person in the list
for person in people:
    # extract variables from the dictionary