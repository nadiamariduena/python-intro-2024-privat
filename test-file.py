foods = ["rice", "tomatoes", "chicken", "vegetables", "dessert"]


calories = [200, 30, 300, 100, 150]

total_calories = 0

for i in range(len(foods)):
    total_calories += calories[i]
    print(f"{foods[i].capitalize()}: {calories[i]} calories")


print(f"Total calories: {total_calories}")