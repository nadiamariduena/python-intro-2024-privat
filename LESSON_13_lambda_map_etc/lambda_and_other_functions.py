def squared(num): return num + num
print(squared(2))
#result
#4 // num + num or 2 + 2 = 4

#🖐️ here you have to be careful, if you dont add parenthesis to the lambda like here (lambda num : num * num), it will reformat it, and you wont get the result 4
squared = (lambda num1 : num1 * num1)
print(squared(2))
# the reformat happens in line 8, when typing (squared(2))

#
# ------- another example
def addTwo(num): return num + 2

print(addTwo(12))
#result
# 14