# 1. for this example, i will create a new dic

animalss = {
    "anim1": "parrot",
    "anim2": "eagle"
}
fishes = animalss.copy()  # Create a copy of animalss
fishes["anim3"] = "turtle"
print(animalss)
print(fishes)


# result
#{'anim1': 'parrot', 'anim2': 'eagle'}
# {'anim1': 'parrot', 'anim2': 'eagle', 'anim3': 'turtle'}
