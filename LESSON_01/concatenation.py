first = 'Laure'
last = "Blaz"
##its like in js, it concatenate the 2 variables into 1
fullname = first + " " + last
print(fullname)
# in addition you can also add this below, it will add the exclamation to the full name
fullname += "!"
print(fullname)

#🟥 number to string
#I need to convert the number to a string to concatenate it to the fullname

decade = str(1982)
print(type(decade))
print(decade)

## Another example
# add another variable that will contain the previous information
statement = 'I like rock music ' + decade + 's.'
print(statement)


#
#
# 🟠 Multiple lines

multiline = '''
Hey, how are you?

I was just checking in.
                         All good things
'''
print(multiline)