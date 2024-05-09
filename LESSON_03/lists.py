users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptyList = []

print("Dave" in data)

# get an element from a list

print(users[0])
print(users[-1]) # will get the last item
print(users[-2]) # will get the penultimo/second-last
print(users.index('Sara')) # result: position 2
print(users[0:2]) #here we will get the first 2 items of the list
print(users[1:]) # it will pick up the item at position 1 and all after that, the reason for that is because arent specifing a second value after the:colons
#
#
print(users[-3:-1])
print(len(data))