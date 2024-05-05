first = 'Laure'
last = "Blaz"

multiline = '''
Hey, how are you?

I was just checking in.
                         All good things
'''
print(multiline)

#
#
# Escaping special characters
 #
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at \\located'
print(sentence)

#
#
# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)


print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))

#
# White space
# to see the caracters
print(len(multiline.strip()))
# #l for left
print(len(multiline.lstrip()))
# r for right character
print(len(multiline.rstrip()))

print("")

 # Build a Menu
title = "menu".upper()
print(title.center(20, "="))