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
#
messageThree = "\n{} has {} coinss left.".format(person, coins)
print(messageThree)
# Dave has 3 coinss left.