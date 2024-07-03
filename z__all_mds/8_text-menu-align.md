# 🟡 Build a Menu

https://youtu.be/INGJh9DEaBM?feature=shared&t=1310

<br>
<br>

```python
title = "menu".upper()
# ill fill 20 character with '=' and position the title  to the center
print(title.center(20, "="))

#
# RESULT
========MENU========
```

<br>
<br>

# 🟡 Structure Price

```python
# position the coffee to the Left with ljust (justfify content left ) https://developer.mozilla.org/en-US/docs/Web/CSS/justify-self
#
# Add 16 dot character
print('Coffee'.ljust(16, '.') + '$1'.rjust(4))
# add the 1$ to the right with (rjust), leave 4 character between the dots and the 1$
#result
Coffee..........  $1
#
# OR
print('Coffee'.ljust(16, '.') + '$1'.rjust(1))
#See the difference, the space between the dots and the 1$
#result
Coffee..........$1
```

<br>

```python
print("")
 # Build a Menu
title = "menu".upper()
print(title.center(20, "="))
print('Coffee'.ljust(16, '.') + '$1'.rjust(3))
#
#
print('Muffin'.ljust(16, '.') + '$25'.rjust(3))
# space
print("")
# space
extraTitle = "extra expenses".upper()
print(extraTitle.center(20, "="))
print('Eclair'.ljust(16, '.') + '€8'.rjust(3))
#

#
#
#  RESULT

========MENU========
Coffee.......... $1
Muffin..........$25

===EXTRA EXPENSES===
Eclair.......... €8
```

<br>
<br>
