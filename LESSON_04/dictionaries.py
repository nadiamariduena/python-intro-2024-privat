# version 1
band ={

"vocals": "Plant",
"guitar": "Page"

}
print(band)
#result: {'vocals': 'Plant', 'guitar': 'Page'}
#
# version 2

band2 = dict(
vocals="Plant",
guitar="Page"
)

print(band2)
#result: {'vocals': 'Plant', 'guitar': 'Page'}
print(type(band))
#result: <class 'dict'>
print(len(band))
#result: 2

#
# ----- ACCESSing the data ---
# band ={

# "vocals": "Plant",
# "guitar": "Page"

# }
print(band["vocals"])
print(band.get("guitar"))
#result:
# i get plant and page, because these are the values that are aligned to the dictionary in line 27
# Plant
# Page


#
#
# ----- print all keys ---

print(band.keys())
# result: dict_keys(['vocals', 'guitar'])