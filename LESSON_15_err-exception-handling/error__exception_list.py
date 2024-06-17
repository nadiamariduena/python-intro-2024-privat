# ** Built-in Exceptions

## Beginner-friendly examples of handling Python exceptions based on common exceptions from the list provided by W3Schools: https://www.w3schools.com/python/python_ref_exceptions.asp



#
# ** ----- RAISE -----
# - With raise you can custom your error messages
# this is a simple example, later on you can add other conditions like: not allowing the user to type less than 2 or 3 numbers or more than 4, because you want a year , stuff like that

def calculate_age(year_of_birth):
    current_year = 2024
    if year_of_birth > current_year:
        raise ValueError("Year of birth cannot be in the Future ⏰ ⬅️🚗 💨 ⚡️ ")
    return current_year - year_of_birth

try:
    year = int(input("Enter your year of birth:"))
    age = calculate_age(year)
    print(f"You are {age} years old")
except ValueError as new:
    print("Error:", new)

#
# ** ----- Value ERROR -----
#

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Number must be positive")
    print("Number entered:", num)

except ValueError as e:
    print("Invalid input", e)

# OUTPUT
# if you type: -20 or using the minus, its going to be negative, and it will give you this:
# Enter a number: -10
# Invalid input Number must be positive
#
# BUT if you type a positibe number like: 20 , it will give you this:
# Enter a number: 20
# Number entered: 20