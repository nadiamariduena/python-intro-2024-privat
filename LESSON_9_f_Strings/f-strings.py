person = "Dave"

coins = 3

print("\n" + person + " has " + str(coins) + " coins left." )

#
# Lets find another way of creating the same string
message = "\n%s hass %s coins left." % (person, coins)
print(message)
#
#