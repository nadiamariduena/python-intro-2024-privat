# 1. for this example, i will create a new dic

animalss ={
"anim1": "parrot",
"anim2": "eagle"
}
fishes ={
"anim1": "dorada",
"anim2": "espadon"
}
print(animalss)
print(fishes)
#result
# {'anim1': 'parrot', 'anim2': 'eagle'}
# {'anim1': 'dorada', 'anim2': 'espadon'}
#
#
# ---- copy -------
# it s not a good thing to create a copy in such way, because here we are not creating a copy but a reference, and it means that they are both refereeing to the same place in memory or the same dictionary, so if i add or remove somthing to animalss , the fishes will be affected
animalss = fishes # create a reference