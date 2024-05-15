#
# -------
# WHILE LOOP
#---------
#
#
value = 1
while value < 10:
    print(value)
    value += 1

#
#-------
# Another WAY to break the LOOP
#--------
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break #if the condition is met, it will stop the loop at 5
    value += 1