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
#result
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
#
#
# ------ **
print('---- example 2 ----')
#------- **
#
#
# 🖐️ It doesnt reach the 10, because the condition tells that "WHILE" its less than 10. if you want to show the 10, you can change the condition from < 10 to <= 10 (less or equal to 10)
value = 1
while value <= 10:
    print(value)
    value += 1
#result
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
#
# 🖐️ Another WAY to break the LOOP
#--------
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break #if the condition is met, it will stop the loop at 5
    value += 1
    #result
# 1
# 2
# 3
# 4
# 5

#
#
# ------ **
print('---- example 3 ----')
#------- **
#
#
# 🖐️ the 'CONTINUE'
# Here i will re arrange the condition, the reason for that is because i will cut the loop and this loop will continue after a certain point
#
#
