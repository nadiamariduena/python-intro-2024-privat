# ----
import math
#
#
gpa = 3.28
#
#
#
# abs for absolute
print(abs(gpa))
# result: 3.28

# 🟡  ROUND
# -round a floating-point number to the nearest integer.
#
# #rounding the value
# similar to js Math.round() (but they may have slight differences in behavior due to language-specific implementations), check the MD to see the differences

print(abs(gpa * -1))
# result: 3.28
#
print(round(gpa))
# result: 3
print(round(gpa, 1))
# result: 3.3
#
#
#
# gpa = 3.28
# ----- MATH
print(math.pi)
#result: 3.141592653589793
#
# ----- math.SQUARE
print(math.sqrt(64))
# result: 8.0
# ----- math.CEIL
print(math.ceil(gpa))
# result: 4
# ----- math.floor
print(math.floor(gpa))
# result: 3

#
#
# -------
# Casting a string to a number
zipcode = "1001"
zip_value = int(zipcode)
print(type(zip_value))
# result: <class 'int'>

#
#
# Error if you attempt to cast incorrect data
# check on the terminal what happens when you try to add the below, its a different type and you will get an error:
zip_value = int("New York")
