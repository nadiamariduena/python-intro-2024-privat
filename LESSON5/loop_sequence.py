
# ------ **
print('---- example 8 ----')
#------- **
#
# LOOP over the list and check if there is a specific name

thenames = ["Dave", "Sara", "John"]

for px in thenames:
# you will notice that it will jump and continue the loop after sara
    if px == 'Sara':
      continue
    print(px)
# result: Dave, John