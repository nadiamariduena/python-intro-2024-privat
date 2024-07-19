# 🟡 When you use 'w' mode (open('menu.txt', 'w')), it will create the menu.txt file if it doesn't already exist.
# --- will generate
#1 step
menu_file = open("menu.txt", "w")
# ----

# 2 Write the menu items to the file
# Add the stuff below to the generated menu.txt in step 1
menu_file.write("Menu:\n")
menu_file.write("1. 🍨 Chocolate Ice Cream: $3.50\n")
menu_file.write("2. 🍦 Vanilla Ice Cream: $3.00\n")

# after the STEP 1 & 2 run the code, type:  python icecream.py


# Close the file to SAVE the changes

menu_file.close()


#
#
# Reading from a file (displaying menu)
menu_file = open("menu.txt", "r")
menu_content = menu_file.read()
print(menu_content)



