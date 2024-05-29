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