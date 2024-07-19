# 🟡 When you use 'w' mode (open('menu.txt', 'w')), it will create the menu.txt file if it doesn't already exist.
# --- will generate
#1 step
menu_file = open("iceCream_menu.txt", "w")
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
# 3 Reading from a file (displaying menu)
# this block below will be shown in your console when you will run the code again, keep in mind that at this point the menu.txt has been created and the below code will only read and show the stuff you have within the menut.txt
menu_file = open("menu.txt", "r")
menu_content = menu_file.read()
print(menu_content)


# ------------

# 4 Appending to a file (recording orders)

order_file = open("iceCream_orders.txt", "a")
order_file.write("New order: Bubble gum 🍬 Ice Cream, Large\n")
order_file.write("🙆‍♂️ Customer: Alistair")
order_file.close()
