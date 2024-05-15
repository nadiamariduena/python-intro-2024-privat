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
# So, this loop starts with value set to 1, then it iterates over the values from 2 to 10. However, when value equals 5, the continue statement is executed. This means that when value is 5, the loop will skip printing that value and move on to the next iteration.
#

value = 1
while value <= 10:
  value += 1
  if value == 5:
   continue  # If value is 5, the loop skips the remaining code in this iteration and continues to the next iteration

  print(value)
#
# NOTICE how it starts after the 1 and then stops at 5, its because it will continue after the 5
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# 11


# ------ **
print('---- example 3 ----')
#------- **
#
#
## 🖐️ USING the else
#You can use it once the loop is completed and the condition is no longer TRUE

value = 1
while value <= 10:
  value += 1
  if value == 5:
   continue  # If value is 5, the loop skips the remaining code in this iteration and continues to the next iteration

  print(value)